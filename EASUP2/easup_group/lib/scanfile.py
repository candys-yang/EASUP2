# -*- coding: UTF-8 -*-


'''

    模块一经引用，即被执行。
    它会扫描指定目录的文件夹并读取hash保存到数据库。
    
    依赖于： sqlio.py  conf.py

    过程：
        > 清空数据库hash数据
        > 实施扫描
            > 当扫描到一个文件，实施数据库判定

    日期：2019-1-5   作者：杨主任
    Email： 522703331@qq.com 
    GIT：https://github.com/candys-yang/
    blog：http://varmain.com

'''



import sqlio
import conf
import os
import hashlib


#清理数据库hash
sqlio.ClearFileHashSQL()

#获取文件hash
def get_file_md5(f):
    hash_new = hashlib.sha1() #或hashlib.md5() 
    with open(f,'rb') as fp: #打开文件，一定要以二进制打开 
        while True: 
            data = fp.read() #读取文件块 
            if not data: #直到读完文件 
                break 
            hash_new.update(data) 
    hash_value = hash_new.hexdigest() #生成40位(sha1)或32位(md5)的十六进制字符串 
    #匹配hash，若为不匹配，写入数据库
    sqlio.FileHashIs(f,hash_value,True)
    #print (hash_value)


#扫描目录
path=conf.kingdee_dir
print("扫描金蝶目录...")
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
        fullpath=os.path.join(dirpath,file)
        #扫描到的每一个文件都执行hash并处理数据库
        get_file_md5(fullpath)


