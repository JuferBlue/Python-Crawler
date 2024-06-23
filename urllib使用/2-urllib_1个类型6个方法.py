"""
@author:JuferBlue
@file:2-urllib_1个类型6个方法.py
@date:2024/6/23 9:07
@description:
"""
import urllib.request

url = "https://www.jxufe.edu.cn/"

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(url)
# <class 'http.client.HTTPResponse'>

# 一个类型和六个方法

# 1.read() 字节形式读取二进制 扩展：rede(5)返回前几个字节
# print(response.read().decode("utf-8"))

# 2.readline() 读取一行
# print(response.readline())

# 3.readlines() 读取所有行
# print(response.readlines())

# 4.getcode() 获取状态码
print(response.getcode())

# 5.geturl() 获取请求的url
print(response.geturl())

# 6.getheaders() 获取响应头
print(response.getheaders())
