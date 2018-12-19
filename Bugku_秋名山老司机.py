# coding:utf-8
import requests, re

URL = 'http://123.206.87.240:8002/qiumingshan/'

s = requests.Session()
get = s.get(URL, verify=False)
html = get.text

str = re.compile(r'[\*\+\-]*[0-9]{5,}').findall(html)
print(str)
form = ''
for i in str:
    form += i
print(form)
answer = int(eval(form))


post = s.post(URL, data={'value':answer}, verify=False)
print(post.text)
