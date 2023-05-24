from flask import Blueprint, jsonify, send_from_directory
from utils.utils import *
import os

predict_bp = Blueprint('predict', __name__)

root_path = os.environ.get('PROJECT_ROOT')
dir_path = os.path.abspath(os.path.join(root_path, '../model/hands_generator.h5'))
generator = load_generator(dir_path)


@predict_bp.route('/predict', methods=['GET'])
def predict():
    images = generate_images(generator)
    image_paths = generate_images_paths(images)
    return jsonify(image_paths)


@predict_bp.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('/images', filename)