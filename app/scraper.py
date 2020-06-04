from bs4 import BeautifulSoup
from requests import get
cspan_url = 'https://www.c-span.org/search/?sdate=&edate=&searchtype=Videos&sort=Most+Recent+Event&text=0&sponsorid%5B%5D=1133&formatid%5B%5D=33'
response = get(cspan_url)
soup = BeautifulSoup(response.text, 'html.parser')

# find the video link from video page
def get_video_link(link):
  video_response = get(link)
  video_soup = BeautifulSoup(video_response.text, 'html.parser')
  video_title = video_soup.find('h3')
  return video_soup

# scrape the full list of videos
def get_all_videos():
  video_list = soup.find_all('li', {'class': 'onevid'})

  for video in video_list:
    a = video.find('a')
    video_link = 'https:' + a['href'], a.get_text()
    first_video = video_link[0]
  
  print(get_video_link(first_video))
  

get_all_videos()
# scrape the top video
def get_latest_video():
  top_video = {}
  return top_video