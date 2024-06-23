"""
@author:JuferBlue
@file:7-urllib_post请求百度翻译.py
@date:2024/6/23 10:24
@description:
"""

import urllib.request
import urllib.parse

url = "http://cta.jxufe.edu.cn/searchTeachers"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

teacher_name = input("请输入要查询的教师姓名：")


date = {
    'fid':'109051',
    'teaName':teacher_name,
    'researchFields':'',
    'groupname':'',
    'page':'1',
    'pageSize':'10'
}

# post的请求参数必须进行编码
date = urllib.parse.urlencode(date).encode('utf-8')

request = urllib.request.Request(url=url,headers=headers,data=date)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
print(type(content))

# 字符串----》json

import json
result = json.loads(content)
print(type(result))
print(result)
