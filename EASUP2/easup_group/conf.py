# -*- coding: UTF-8 -*-


'''

    该文件定义了 EASUP2 的功能特性。
    配置项遵循 python 语法标准。
    
        修改该文件的配置项，应当采用静态的
    参数值，请勿使用动态的变量或者直接添加
    脚本代码在这里，以免引起性能或不必要的
    异常错误。

    日期：2019-1-5   作者：杨主任
    Email： 522703331@qq.com 
    GIT：https://github.com/candys-yang/
    blog：http://varmain.com

'''


#标准库
import os
import sys

#第三方库

#------------------


# 软件主目录，默认将获取当前所在目录
python_dir = os.getcwd()


# 金蝶目录（请勿修改）
kingdee_dir = 'D:\Kingdee\eas\client'




#文件共享账号与密码
#   perm 参数说明：
'''
Read permissions:
“e” = change directory (CWD, CDUP commands)
“l” = list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)
“r” = retrieve file from the server (RETR command)
Write permissions:
“a” = append data to an existing file (APPE command)
“d” = delete file or directory (DELE, RMD commands)
“f” = rename file or directory (RNFR, RNTO commands)
“m” = create directory (MKD command)
“w” = store a file to the server (STOR, STOU commands)
“M” = change file mode / permission (SITE CHMOD command)New in 0.7.0
“T” = change file modification time (SITE MFMT command) New in 1.5.3
官方文档: http://pyftpdlib.readthedocs.io/en/latest/api.html
'''
ftpd_user = ''
ftpd_pwd = ''
ftpd_dir = str(os.getcwd()) + '\web'
ftpd_perm = 'elr'                       #默认只读权限（elr）
ftpd_ip = '127.0.0.1'                   #集团端服务器ip
ftpd_port= 10861



