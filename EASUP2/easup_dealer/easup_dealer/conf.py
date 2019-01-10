# -*- coding: UTF-8 -*-


'''

    该文件定义了 EASUP2 的功能特性。
    配置项遵循 python 语法标准。
    
        修改该文件的配置项，应当采用静态的
    参数值，请勿使用动态的变量或者直接添加
    脚本代码在这里，以免引起性能或不必要的
    异常错误。

    日期：2019-1-8   作者：杨主任
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

# 集团端服务器信息
ftpser_ip = ''
ftpser_port = 
ftpser_user = ''
ftpser_pwd = ''



#启动软件时，不清空web的金蝶文件
#   当为 True 时，店端的金蝶目录将不会被清理
#   当为 False 时，店端的金蝶目录将被清理，并从集团端拉取完整更新。
each_run_update_eas_file = True



#文件分发服务
#   店内网络管理员无需修改。
ftpd_user = ''
ftpd_pwd = ''
ftpd_dir = str(os.getcwd()) + '\web'
ftpd_perm = 'elr'                       
ftpd_ip = '0.0.0.0'                   
ftpd_port= 10861

