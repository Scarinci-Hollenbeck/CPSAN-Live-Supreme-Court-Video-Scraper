# from dotenv import load_dotenv
import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

from models import setup_db, Videos, db


#----------------------------------------------------------------------------#
# App & Database config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
CORS(app, resources={'/': {'origins': '*'}})
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Routes.
#----------------------------------------------------------------------------#

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET')
  return response

# Get video list 
@app.route('/videos', methods=['GET'])
def get_videos():
  # videos = Videos.query.all()
  # all_videos = [video.format() for video in videos]

  try:
    return jsonify({
      'success': True,
      'videos': 'videos'
    })
  except:
    abort(404)

# Get the latest video
@app.route('/latest-video', methods=['GET'])
def get_latest_video():
  # latest_video = Videos.query.all() # change to query by date
  try:
    return jsonify({
      'success': True,
      'videos': 'get the latest video'
    })
  except:
    abort(404)

