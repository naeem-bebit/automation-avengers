from flask import Flask, request, render_template_string, render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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

    return render_template("index.html")

@app.route('/klazan')
def klazan_page():
    logger.info('KLAzan page accessed')

    return render_template("klazan.html")

@app.route('/newpage')
def new_page():
    logger.info('New page accessed')
    return render_template("newpage.html")

if __name__ == '__main__':
    logger.info('Starting the Flask application')
    app.run()
