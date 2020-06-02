import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from models import setup_db, Videos

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={'/': {'origins': '*'}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

  # Get video list 
  @app.route('/videos', methods=['GET'])
  def get_videos(payload):
    videos = Videos.query.all()
    all_videos = [video.format() for video in videos]

    try:
      return jsonify({
        'success': True,
        'videos': all_videos
      })
    except:
      abort(404)
