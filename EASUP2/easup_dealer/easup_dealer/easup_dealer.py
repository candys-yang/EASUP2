# -*- coding: UTF-8 -*-





'''

    这是软件的主入口

    日期：2019-1-8   作者：杨主任
    Email： 522703331@qq.com 
    GIT：https://github.com/candys-yang/
    blog：http://varmain.com

'''




#标准库
import os
import sys,json
#第三方库


#本地库
import conf



# ------------ 初始化指令 ------------
# 模块搜索
sys.path.append(conf.python_dir + "/lib")
import ftpc
import fileupdate

downfile = []

policystr = ""

#下载关键文件列表到web目录
print("Get KeyFile For GroupServer...")
#print("filelist.json copying...")
#ftpc.Downloadfile('filelist.json','web\\filelist.json')
print("policy.txt copying...")
ftpc.Downloadfile('policy.txt','web\\policy.txt')
#print("Loading File List Data ...")
#filelistjson = open('web\\filelist.json').read()

#序列化文件列表
#downfile = json.loads(filelistjson)
#策略文件字符化
policystr = open('web\\policy.txt')

'''
eruef = True
try:
    if sys.argv[1] == '1':
        eruef = False
except :
    eruef = True
'''

#实施更新措施
if conf.each_run_update_eas_file:
    print("当前参数设定，不清空金蝶目录...")
    print("update file:")
    #遍历服务器文件列表数据。
    fileupdate.updatefile()
else:
    print("当前参数设定，清空金蝶目录...")
    fileupdate.Delclient()
    fileupdate.updatefile()

__import__("ftpd")
