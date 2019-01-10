# -*- coding: UTF-8 -*-


import conf

# FTP操作
import ftplib , os


f = ftplib.FTP()
f.connect(conf.ftpser_ip,conf.ftpser_port)
f.login(conf.ftpser_user, conf.ftpser_pwd)  # 登录
pwd_path = f.pwd()
print("Link To Group Server Root:", pwd_path)


def Downloadfile(remotepath, localpath):
    bufsize = 4096                #设置缓冲块大小
    p = os.path.split(localpath)
    #print("mkdir " + p[0])
    if not os.path.exists(p[0]):
        try:    
            os.makedirs(p[0])
        except :
            print("mkdir fail：" + p[0])
    #print("create: " + localpath)

    try:
        fp = open(localpath,'wb')     #以写模式在本地打开文件
        f.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    except :
        print("create fail: " + localpath)
    f.set_debuglevel(0)         #关闭调试
    fp.close()                    #关闭文件
    
    


