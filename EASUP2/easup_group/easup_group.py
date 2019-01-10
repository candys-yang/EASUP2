# -*- coding: UTF-8 -*-


'''

    这是软件的主入口
    当该文件运行时，将会根据 conf.py 文件进行一系列的数据处理。

    日期：2019-1-5   作者：杨主任
    Email： 522703331@qq.com 
    GIT：https://github.com/candys-yang/
    blog：http://varmain.com

'''




#标准库
import os
import sys

#第三方库
import shutil

#本地库
import conf
# ------------ 初始化指令 ------------
# 模块搜索
sys.path.append(conf.python_dir + "/lib")
import fileio

#扫描hash并重建数据库hash表数据
__import__('scanfile')

#操作文件...
fileio.KillKingdee()
fileio.Delclient()
fileio.Copyclient()
fileio.CpDataFile()
#开启文件服务
__import__('ftpd')


