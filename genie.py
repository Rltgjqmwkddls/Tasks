import requests
from bs4 import BeautifulSoup

def genie(num):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    site = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg={num}'
    request = requests.get(site, headers=header)
    soup = BeautifulSoup(request.text, 'html.parser')
    titles = soup.findAll('a', {'class':'title ellipsis'})
    artists = soup.findAll('a', {'class':'artist ellipsis'})
    data = []
    for title, artist in zip(titles, artists):
        title_text = title.text.strip()
        artist_text = artist.text.strip()
        data.append({'title': title_text, 'artist': artist_text})

    return data

all_data = []

for num in range(1, 5):  # 1페이지부터 4페이지까지 순회
    page_data = genie(num)
    all_data.extend(page_data)

# 1위부터 200위까지 출력
for rank, entry in enumerate(all_data, start=1):
    print(f"{rank}위: {entry['title']} - {entry['artist']}")