from flask import Flask, render_template
import tensorflow as tf
from utils.utils import *

import os

os.environ['PROJECT_ROOT'] = os.path.dirname(os.path.abspath(__file__))


from routes.prediction import predict_bp


if __name__ == '__main__':  

    app = Flask(__name__)

    @app.route('/')
    def index_page():
        return render_template('index.html')


    @app.after_request
    def add_cache_control_headers(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

  
    app.register_blueprint(predict_bp)
    app.run()