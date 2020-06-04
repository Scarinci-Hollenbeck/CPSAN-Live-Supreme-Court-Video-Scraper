from bs4 import BeautifulSoup
from requests import get
cspan_url = 'https://www.c-span.org/search/?sdate=&edate=&searchtype=Videos&sort=Most+Recent+Event&text=0&sponsorid%5B%5D=1133&formatid%5B%5D=33'
response = get(cspan_url)
soup = BeautifulSoup(response.text, 'html.parser')

# scrape the full list of videos
def get_all_videos():
  video_list_container = soup.find_all('li', {'class': 'onevid'})
  video_list = []


  for index, video in enumerate(video_list_container):
    '''
    retrieve the video's link
    '''
    a = video.find('a')
    video_link = 'https:' + a['href'], a.get_text()[0]
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

    video = {
      'id': index,
      'title': h3.get_text(),
      'date': time.get_text(),
      'video_link': stand_alone_video_link
    }
    video_list.append(video)
  
  print(video_list)
    
  

get_all_videos()
# scrape the top video
def get_latest_video():
  top_video = {}
  return top_video