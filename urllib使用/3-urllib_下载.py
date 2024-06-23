"""
@author:JuferBlue
@file:3-urllib_下载.py
@date:2024/6/23 9:18
@description:
"""

import urllib.request

# 下载一个网页
# url_page = "https://www.jxufe.edu.cn/"
# urllib.request.urlretrieve(url_page, "jxufe.html")# 两个参数：url,保存文件名

# 下载图片
# url_img = "https://tse2-mm.cn.bing.net/th/id/OIP-C.jKQ-BSKYnwEyLGx5bcNgJQHaE5?w=262&h=180&c=7&r=0&o=5&pid=1.7"
# urllib.request.urlretrieve(url_img, "jxufe.jpg")

# 下载视频
url_video = "https://vdept3.bdstatic.com/mda-pbf3xzqm3fffa9p6/cae_h264/1676522373660816034/mda-pbf3xzqm3fffa9p6.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1719117175-0-0-fbad19e3601084b74eb75519e41c47db&bcevod_channel=searchbox_feed&cr=0&cd=0&pd=1&pt=3&logid=1975700540&vid=10290936590942910407&klogid=1975700540&abtest="
urllib.request.urlretrieve(url_video, "jxufe.mp4")

