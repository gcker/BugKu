#-*- coding:utf-8 -*-
#网络安全实验室-脚本关-第二关
import requests
import re
from html.parser import HTMLParser

#编辑头部信息
head = {'cookie':'PHPSESSID=7b646f016c33985961c495fca147326e'}
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'

#获取算式
r = requests.get(url, headers=head)
html = r.text
formula = re.compile(r'[0-9\-\+*/\(]+[)]').findall(html)[0]
# print(formula)

#计算答案
res = eval(formula)
# print(res)

#发送答案
r = requests.post(url, data={'v':res}, headers=head)
print(r.text)
