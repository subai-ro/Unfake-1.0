import sys
import logging
from app import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add error handlers
@app.errorhandler(500)
def handle_500(error):
    logger.error(f'Server error: {error}')
    return str(error), 500

@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f'Unhandled exception: {error}')
    return str(error), 500

if __name__ == "__main__":
    try:
        logger.info('Starting application...')
        app.run()
    except Exception as e:
        logger.error(f'Failed to start application: {e}')
        sys.exit(1) 