# from dotenv import load_dotenv
import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
from models import setup_db, db, Videos
from scraper import scrape_all_videos, scrape_latest_video

def create_app(test_config=None):
  #----------------------------------------------------------------------------#
  # App config.
  #----------------------------------------------------------------------------#
  app = Flask(__name__, instance_relative_config=True)
  setup_db(app)
  CORS(app, resources={'/': {'origins': '*'}})
  
  # ensure the instance folder exists
  try:
      os.makedirs(app.instance_path)
  except OSError:
      pass

  #----------------------------------------------------------------------------#
  # Routes.
  #----------------------------------------------------------------------------#
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response
  
  # get all videso
  @app.route('/supreme-court-videos/all', methods=['GET'])
  def all_videos():
    videos = Videos.query.all()

    if len(videos) == 0:
      try:
        scraped_videos = scrape_all_videos()

        for video in scraped_videos:
          new_video = Videos(title=video['title'], date=video['date'], slug=video['slug'], video_link=video['video_link'])
          db.session.add(new_video)
          db.session.commit()

      except:
        db.session.rollback()

      finally:
        db.session.close()

        videos_from_db = Videos.query.order_by(Videos.id).all()
        formatted_videos = [video.format() for video in videos_from_db]
        video_list = formatted_videos

    else:
      # check if video list is updated      

      # slug from latest scraped record
      latest_scraped_video = scrape_latest_video()
      scraped_slug = latest_scraped_video['slug']

      # check if scraped slug exists in db
      find_latest_slug_by_scraped_slug = bool(Videos.query.filter_by(slug=scraped_slug).first())

      if find_latest_slug_by_scraped_slug == False:
        try:
          add_latest_video = Videos(title=latest_scraped_video['title'], date=latest_scraped_video['slug'], slug=scraped_slug, video_link=latest_scraped_video['video_link'])
          db.session.add(add_latest_video)
          db.session.commit()
        except:
          db.session.rollback()
        finally:
          db.session.close()

          videos_from_db = Videos.query.order_by(Videos.id).all()
          formatted_videos = [video.format() for video in videos_from_db]
          video_list = formatted_videos
      else:
        videos_from_db = Videos.query.order_by(Videos.id).all()
        formatted_videos = [video.format() for video in videos_from_db]
        video_list = formatted_videos      
    
    return jsonify({
      'success': True,
      'videos': video_list
    })

  @app.route('/supreme-court-videos/latest', methods=['GET'])
  def get_the_latest_video():
    # slug from latest scraped record
    latest_scraped_video = scrape_latest_video()
    scraped_slug = latest_scraped_video['slug']

    # check if scraped slug exists in db
    find_latest_slug_by_scraped_slug = bool(Videos.query.filter_by(slug=scraped_slug).first())

    if find_latest_slug_by_scraped_slug == False:
      try:
          add_latest_video = Videos(title=latest_scraped_video['title'], date=latest_scraped_video['slug'], slug=scraped_slug, video_link=latest_scraped_video['video_link'])
          db.session.add(add_latest_video)
          db.session.commit()
      except:
        db.session.rollback()
      finally:
        db.session.close()
        latest_video = Videos.query.filter_by(slug=scraped_slug).first()
    else:
      latest_video = Videos.query.filter_by(slug=scraped_slug).first()

    return jsonify({
      'success': True,
      'videos': {
        'id': latest_video.id,
        'title': latest_video.title,
        'date': latest_video.date,
        'slug': latest_video.slug,
        'video_link': latest_video.video_link
      }
    })
 
  if __name__ == "__main__":
    app.run()