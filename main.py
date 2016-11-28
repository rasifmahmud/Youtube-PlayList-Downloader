import requests
from bs4 import BeautifulSoup
from pytube import YouTube
url = 'https://www.youtube.com/watch?v=givuYd_cKm0&list=PL6gx4Cwl9DGD25IGk9Xf7oC3wiT9gC75x'
source_code = requests.get(url, allow_redirects=False)
plain_text = source_code.text.encode('ascii', 'replace')
soup = BeautifulSoup(plain_text, 'html.parser')
list = []
for link in soup.findAll('li', {'class': 'yt-uix-scroller-scroll-unit '}):
    id = link.get('data-video-id')
    list.append(id)



counter=0

#index number 48 is missing to download
#another one missing may be 9 or 10 or 11
for i in range(len(list)):
    id = 'https://www.youtube.com/watch?v='+list[i]
    yt = YouTube(id)
    video = yt.get('mp4', '720p')
    video.download('photoshop'+str(counter))
    print(counter)
    counter=counter+1


