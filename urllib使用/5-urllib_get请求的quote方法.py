"""
@author:JuferBlue
@file:5-urllib_get请求的quote方法.py
@date:2024/6/23 9:54
@description:
"""
import urllib.request
import urllib.parse

# 周杰伦不能被ascii编码
# url = "https://www.baidu.com/s?wd=周杰伦"
url = "https://www.baidu.com/s?wd="


# 模拟浏览器向服务器发送请求
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# 将周杰伦三个字编变成unicode编码格式
url = url + urllib.parse.quote("周杰伦")

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 获取内容
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)

