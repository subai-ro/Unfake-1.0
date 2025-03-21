# Unfake - Fake News Detection Platform

A web application for detecting and managing fake news articles using machine learning and community ratings.

## Features

- User authentication and profiles
- Article submission and rating system
- Machine learning-based fake news detection
- Admin panel for content moderation
- Comprehensive statistics and analytics
- Category-based article organization

## Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd unfake
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python schema_creation.py
```

5. Run the application:
```bash
python app.py
```

## Deployment to Render

1. Push your code to a Git repository (GitHub, GitLab, or Bitbucket)

2. Sign up for a Render account at https://render.com

3. Create a new Web Service:
   - Connect your Git repository
   - Select the repository
   - Configure the service:
     - Name: unfake
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
     - Python Version: 3.9.0

4. Add environment variables in Render:
   - `FLASK_ENV`: production
   - `SECRET_KEY`: (generate a secure random key)

5. Deploy the service

## Database

The application uses SQLite for local development. For production, consider using a more robust database like PostgreSQL.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 