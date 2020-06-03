# from dotenv import load_dotenv
import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#----------------------------------------------------------------------------#
# App & Database config.
#----------------------------------------------------------------------------#

# load_dotenv()

# db_password=os.getenv("db_password")
# db_username=os.getenv("db_username")
# db_database=os.getenv("db_database")
# db_port=os.getenv("db_port")
# db_host=os.getenv("db_host")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:web_scraper_root@localhost:3306/supreme_court_videos'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Videos(db.Model):
  __tablename__ = 'videos'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(1000), nullable=False)
  date = db.Column(db.String(500), nullable=False)
  video_link = db.Column(db.String(2000), nullable=False)

  def __repr__(self):
    return f'ID {self.id}, Title {self.title}, Date {self.date}, Video Link {self.video_link}'



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
  videos = Videos.query.all()
  # all_videos = [video.format() for video in videos]

  try:
    return jsonify({
      'success': True,
      'videos': videos
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

