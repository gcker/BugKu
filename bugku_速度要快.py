import requests, re, base64

URL = 'http://123.206.87.240:8002/web6/'

#创建会话
s = requests.Session()
get = s.get(URL)

#在头部获取flag
flag = get.headers['flag']
#print(flag)

#对获取的flag进行base64解码
flag = base64.b64decode(flag)
flag = str(flag, encoding="utf=8")
flag = flag[15:]
flag = base64.b64decode(flag)

#发送flag值
post = s.post(URL, data={'margin':flag})
print(post.text)
