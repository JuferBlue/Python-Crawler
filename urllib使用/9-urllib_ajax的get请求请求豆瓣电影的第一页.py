"""
@author:JuferBlue
@file:9-urllib_ajax的get请求请求豆瓣电影的第一页.py
@date:2024/6/23 11:37
@description:
"""
import urllib.request
import urllib.parse

# get请求
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(type(content))
print(content)

# 数据写入本地
with open('douban.json','w',encoding='utf-8') as f:
    f.write(content)
