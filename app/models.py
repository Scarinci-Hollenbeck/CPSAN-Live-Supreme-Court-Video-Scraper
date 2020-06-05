from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:web_scraper_root@localhost:3306/supreme_court_videos'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

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
