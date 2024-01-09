import requests   #下载器
import time

# 设置请求头  
headers = {  
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'  
}

url = 'https://movie.douban.com/top250'

r = requests.get(url, headers=headers)

print(r.status_code)

print(r.encoding)

print(r.text)

print(r.headers)

print(r.url)

print(r.content)

print(r.cookies)



