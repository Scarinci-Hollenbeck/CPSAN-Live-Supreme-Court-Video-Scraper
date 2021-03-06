from bs4 import BeautifulSoup
from requests import get

cspan_url = 'https://www.c-span.org/search/?sdate=&edate=&searchtype=Videos&sort=Most+Recent+Event&text=0&sponsorid%5B%5D=1133&formatid%5B%5D=33'
response = get(cspan_url)
soup = BeautifulSoup(response.text, 'html.parser')


# format videos
def formatted_video(video):
  '''
  retrieve the video's link
  '''  
  a = video.find('a')
  video_link = 'https:' + a['href'], a.get_text()
  video_link = video_link[0]
  org = video_link.find('/video/')
  stand_alone_video_link = video_link[:org + len('/video/')] + 'standalone/' + video_link[org + len('/video/'):]

  '''
  retrieve the video's title
  '''
  h3 = video.find('h3')

  '''
  retrieve the video's date
  '''
  time = video.find('time')

  '''
  retrieve the video's slug
  '''
  slug_place = video_link.find('-1/')
  slug = video_link[slug_place + len('-1'):]
  
  '''
  return video details
  '''
  return {
    'title': h3.get_text(),
    'date': time.get_text(),
    'slug': slug,
    'video_link': stand_alone_video_link
  }

# scrape the full list of videos
def scrape_all_videos():
  video_list_container = soup.find_all('li', {'class': 'onevid'})
  video_list = []

  for video in video_list_container:
    video_list.append(formatted_video(video))
   

  return video_list

# get the latest video
def scrape_latest_video():
  latest_video = soup.find('li', {'class': 'onevid'})
  return formatted_video(latest_video)
