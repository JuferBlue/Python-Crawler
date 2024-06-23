"""
@author:JuferBlue
@file:8-urllib_百度翻译之详细翻译.py
@date:2024/6/23 11:12
@description:
"""

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'cookie':'BIDUPSID=13A8AB625D499C8DEBCA1090B6AD4968; PSTM=1719107197; BAIDUID=13A8AB625D499C8D22347E2796B8885D:FG=1; BAIDUID_BFESS=13A8AB625D499C8D22347E2796B8885D:FG=1; BA_HECTOR=a12ka485al8h05a58l01al80a04i371j7evjv1v; ZFY=4:AnNl1lEhnS4349WahbP3oFvwXc5Aki1QGl:A8BEnRD0:C; H_PS_PSSID=60325_60339_60366; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=993cd528-55bd-4e77-be31-aa828f105102&ss=lxqx4vbh&sl=1&tt=204&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2sb&ul=7wc&hd=7zc"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1719109049; APPGUIDE_10_7_1=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1719112410; ab_sr=1.0.1_MWUyM2NkMzg0ZjU3MDAwZjEyNDYzMTEwN2ZlZGQyNjM1MDUxZWY3NjAzYjZkN2VkOTQ3NTA3ZmY5ODVmYjBiMDZmOWNkMzhiOTdkYjhlMTNhOWMwNDcxZTY1ZjBlODlmMWI2NTU4MDNkYzQ4NTdjZjI4YmRjYmY0NTIyNmUxZTlhNGU2MmY4OTc3ZDgxZTBjNDVkNGEyYmJhNTgzM2ViMQ=='
}

data = {
    "from": "en",
    "to": "zh",
    "query": "spider",
    "transtype": "enter",
    "simple_means_flag": 3,
    "sign": "63766.268839",
    "token": "96720990e7002a722d956f06176ff907",
    "domain": "common",
    "ts": "1719112428268"
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json
result = json.loads(content)
print(result)


