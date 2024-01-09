# 导入必要的模块
import requests
from bs4 import BeautifulSoup 

url = 'https://movie.douban.com/top250'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    movie_list = soup.select('span.title')
    print(movie_list)

    chinese_movie_names = [movie.text for movie in movie_list if not movie.text.strip().startswith('/')]

    for index, movie in enumerate(chinese_movie_names, start=1):
        print(f"{index}. {movie}")
    


