"""
@author:JuferBlue
@file:1-urllib_基本使用.py
@date:2024/6/23 8:52
@description:
"""

#使用urllib获取百度首页的源码
import urllib.request

#定义要访问的url
url = 'https://www.jxufe.edu.cn/'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#获取响应中的页面的源码
#read 返回的是二进制的字节数据
html = response.read().decode('utf-8')

print(html)