# -*- coding: UTF-8 -*-


#标准库
import os
import sys
import json
import psutil
#第三方库
import shutil

#本地库
import conf
import sqlio

def Delclient():
    if os.path.exists(conf.python_dir + '\web\client'):
        try:
            print("清空金蝶文件分发目录...")
            shutil.rmtree(conf.python_dir + '\web\client')
        except :
            try:
                print("删除失败，尝试第二次：重新实施删除")
                shutil.rmtree(conf.python_dir + '\web\client')
            except :
                try:
                    print("删除失败，尝试第三次：重新实施删除")
                    shutil.rmtree(conf.python_dir + '\web\client')
                except :
                    print("无法完成文件发布，请自检：")
                    print("1.确保web目录没有被打开，包括子目录")
                    print("2.确保web目录的文件有读写权限")
                    print("")
    else:
        print("不存在 client 目录！！！进行下一步...")
    pass




def Copyclient():
    print("正在实施 复制金蝶到文件分发目录...")
    try:
        shutil.copytree(conf.kingdee_dir, conf.python_dir + '\web\client')
    except :
        print("复制过程发生异常！")
    pass



def KillKingdee():
    '''
    查找金蝶进程，并且结束进程。 
    查找实例：javaw.exe 、easservice
    检索路径关键词：Kingdee
    '''
    print("寻找金蝶服务进程...")
    try:
        print (psutil.pids())
        for x in psutil.pids():
            p = psutil.Process(x)
            print(p.name)#debug
            if p.name() == "javaw.exe":
                print(p.exe())
                cwd = p.cwd()
                print(cwd.find("Kingdee"))
                if cwd.find("Kingdee") >= 1:
                    print("进程符合被杀死的条件，执行命令...")
                    import subprocess,time
                    subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i"%x , shell=False)
                    time.sleep(5)
            if p.name() == "easservice.exe":
                print("发现Debug模式的金蝶驻守进程...")
                print("进程符合被杀死的条件，尝试执行命令...")
                import subprocess,time
                subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i"%x , shell=False)
                time.sleep(5)
    except:
        print(sys.exc_info()[0])
        print("无法关闭金蝶进程...")
    print("过程完成，进行下一步...")
    pass



def CpDataFile():

    sqldata = []
    sqldata =  sqlio.FileListOut() 
    
    #sqldata[0][1]  sqldata[0][0]

    
    f = open(conf.ftpd_dir + "\\filelist.json","w")
    f.write(json.dumps( sqldata, ensure_ascii=False))
    f.close()
    pass