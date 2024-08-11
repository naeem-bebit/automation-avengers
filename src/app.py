from flask import Flask, request, render_template_string
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up a rotating file handler
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.before_request
def log_request_info():
    logger.info(f'Request: {request.method} {request.url}')
    logger.debug(f'Headers: {request.headers}')
    logger.debug(f'Body: {request.get_data()}')

@app.after_request
def log_response_info(response):
    logger.info(f'Response: {response.status}')
    return response

@app.errorhandler(Exception)
def log_exception(e):
    logger.error(f'Exception: {e}', exc_info=True)
    return 'An error occurred', 500

@app.route('/')
def hello_world():
    logger.info('Home page accessed')
    return '''
    Hello, World!
    <form action="/newpage">
        <input type="submit" value="Go to New Page" />
    </form>
    '''

@app.route('/newpage')
def new_page():
    logger.info('New page accessed')
    return 'Welcome to the new page! test again jenkins again, yes again'

if __name__ == '__main__':
    logger.info('Starting the Flask application')
    app.run()
