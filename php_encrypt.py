# coding:utf-8

import base64
import hashlib

'''
A = data
B = flag
C = char
D = 128

'''

def encrypt(data, key): #加密算法
    key = hashlib.md5('ISCC'.encode('utf-8')).hexdigest()
    x = 0
    len = len(data)
    klen = len(key)
    
    chars = []
    str = ''
    
    for i in range(len):
        if (x == klen):
            x = 0
        chars.append(key[x])
        x += 1
    
    for i in range(len):
        str += chr((ord(data[i]) + ord(chars[i])) % 128)
    
    return base64.b64encode(str)
    
str = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='


def decrypt(str):
    str_de = base64.b64decode(str)
    int_str = []
    
    for i in range(len(str_de)):
        int_str.append(str_de[i])
#     print(len(int_str))
    
    key = '729623334f0aa2784a1599fd374c120d729623'
    int_key = []
    for i in range(len(key)):
        int_key.append(ord(key[i]))
#     print(len(int_key))
#     exit(0)
    flag = ''
    for i in range(len(int_str)):
        flag += chr((int_str[i]-int_key[i]+128) % 128)
    print(flag)
    
decrypt(str)
    
    
    
    