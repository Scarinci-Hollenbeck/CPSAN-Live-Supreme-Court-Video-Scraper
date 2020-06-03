from bs4 import BeautifulSoup
from requests import get
cspan_url = 'https://www.c-span.org/search/?sdate=&edate=&searchtype=Videos&sort=Most+Recent+Event&text=0&sponsorid%5B%5D=1133&formatid%5B%5D=33'
response = get(cspan_url)
soup = BeautifulSoup(response.text, 'html.parser')


# scrape the full list of videos
def get_all_videos():
  video_list = []
  return video_list 


# scrape the top video
def get_latest_video():
  top_video = {}
  return top_video 


# find the video link from video page
def get_video_link(link):
  return link