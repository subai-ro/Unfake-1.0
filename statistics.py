from db import get_connection
from datetime import datetime, timedelta

def get_admin_statistics():
    """Get comprehensive statistics for admin panel"""
    conn = get_connection()
    cur = conn.cursor()
    
    # Get user registration statistics
    cur.execute("""
        SELECT DATE(join_date) as date, COUNT(*) as count
        FROM users
        GROUP BY DATE(join_date)
        ORDER BY date DESC
        LIMIT 30
    """)
    user_registrations = cur.fetchall()
    
    # Get article submission statistics
    cur.execute("""
        SELECT DATE(publication_date) as date, COUNT(*) as count
        FROM articles
        GROUP BY DATE(publication_date)
        ORDER BY date DESC
        LIMIT 30
    """)
    article_submissions = cur.fetchall()
    
    # Get rating statistics
    cur.execute("""
        SELECT DATE(rating_date) as date, 
               COUNT(*) as total_ratings,
               AVG(rating_value) as avg_rating
        FROM ratings
        GROUP BY DATE(rating_date)
        ORDER BY date DESC
        LIMIT 30
    """)
    rating_stats = cur.fetchall()
    
    # Get category distribution
    cur.execute("""
        SELECT c.category_name, COUNT(ac.article_id) as article_count
        FROM categories c
        LEFT JOIN article_category ac ON c.category_id = ac.category_id
        GROUP BY c.category_name
    """)
    category_distribution = cur.fetchall()
    
    # Get fake vs real article ratio
    cur.execute("""
        SELECT is_fake, COUNT(*) as count
        FROM articles
        GROUP BY is_fake
    """)
    fake_real_ratio = cur.fetchall()
    
    conn.close()
    
    return {
        'user_registrations': user_registrations,
        'article_submissions': article_submissions,
        'rating_stats': rating_stats,
        'category_distribution': category_distribution,
        'fake_real_ratio': fake_real_ratio
    }

def get_user_statistics(user_id):
    """Get statistics for a specific user"""
    conn = get_connection()
    cur = conn.cursor()
    
    # Get user's rating history
    cur.execute("""
        SELECT DATE(rating_date) as date,
               COUNT(*) as total_ratings,
               AVG(rating_value) as avg_rating
        FROM ratings
        WHERE user_id = ?
        GROUP BY DATE(rating_date)
        ORDER BY date DESC
        LIMIT 30
    """, (user_id,))
    rating_history = cur.fetchall()
    
    # Get user's most rated categories
    cur.execute("""
        SELECT c.category_name, COUNT(*) as rating_count
        FROM ratings r
        JOIN article_category ac ON r.article_id = ac.article_id
        JOIN categories c ON ac.category_id = c.category_id
        WHERE r.user_id = ?
        GROUP BY c.category_name
        ORDER BY rating_count DESC
        LIMIT 5
    """, (user_id,))
    top_categories = cur.fetchall()
    
    # Get user's rating distribution
    cur.execute("""
        SELECT rating_value, COUNT(*) as count
        FROM ratings
        WHERE user_id = ?
        GROUP BY rating_value
        ORDER BY rating_value
    """, (user_id,))
    rating_distribution = cur.fetchall()
    
    # Get user's contribution stats
    cur.execute("""
        SELECT 
            COUNT(DISTINCT r.article_id) as articles_rated,
            COUNT(DISTINCT a.article_id) as articles_submitted,
            AVG(r.rating_value) as average_rating_given
        FROM users u
        LEFT JOIN ratings r ON u.user_id = r.user_id
        LEFT JOIN articles a ON u.user_id = a.submitter_id
        WHERE u.user_id = ?
    """, (user_id,))
    contribution_stats = cur.fetchone()
    
    conn.close()
    
    return {
        'rating_history': rating_history,
        'top_categories': top_categories,
        'rating_distribution': rating_distribution,
        'contribution_stats': contribution_stats
    } 