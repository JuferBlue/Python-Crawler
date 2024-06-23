"""
@author:JuferBlue
@file:4-urllib_请求对象的定制.py
@date:2024/6/23 9:34
@description:
"""
import urllib.request
url = "https://www.baidu.com"


# url组成
# http/https www.baidu,com  80/443   xxx    wd=python    #
# 协议         主机           端口号   路径   参数          锚点
# http 80
# https 443

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
# 请求对象的定制,为了加入伪装标头，伪装成真的浏览器
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)


