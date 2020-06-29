import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine

db = SQLAlchemy()
db_path = 'mysql+pymysql://ptums:db$S&_H1100@localhost:3306/supreme_court_videos'

def setup_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = db_path
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Videos(db.Model):
  __tablename__ = 'videos'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  date = Column(String)
  slug = Column(String)
  video_link = Column(String)

  def __init__(self, title, date, slug, video_link):
    self.title = title
    self.date = date
    self.slug = slug
    self.video_link = video_link
    
  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'date': self.date,
      'slug': self.slug,
      'video_link': self.video_link
    }
  