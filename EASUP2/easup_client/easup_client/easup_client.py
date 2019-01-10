# -*- coding: UTF-8 -*-

import socket,os,sys,ftplib,json

######## 配置数据 (引用的函数：Downloadfile）
conf_dealerser = ""
conf_dealerser_user = ""
conf_dealerser_pwd = ""
conf_dealerser_port = 10861

get_service_address_form_group = False

#这块代码暂时不完善
#如果EASUP客户端文件名不标准，这里将退出程序。
#如果符合标准，将改写 conf_dealerser 的ip地址为文件名的ip
try:
    curfile = sys.argv[0][sys.argv[0].rfind(os.sep) + 1:]
    #从文件名中提取服务器地址
    str_start = curfile.find("@")
    str_end = curfile.find("@",str_start+1)
    ip = curfile[str_start+1:str_end]
    conf_dealerser = ip
    if str_end == -1:
        raise Exception("找不到@或不完整")
except :
    print("文件命名不标准，正确为： EASUP2.0@店内服务器ip地址@.exe")
    print("可联系网络管理员协助处理。")
    print("按Enter键退出...")
    input()
    exit()


def Downloadfile(remotepath, localpath):
    ''' 文件下载，远程目录（远程默认为根），本地目录 '''
    f = ftplib.FTP()
    f.connect(conf_dealerser,conf_dealerser_port)
    f.login(conf_dealerser_user, conf_dealerser_pwd)  # 登录
    pwd_path = f.pwd()
    bufsize = 4096                #设置缓冲块大小
    p = os.path.split(localpath)
    #print("mkdir " + p[0])
    if not os.path.exists(p[0]):
        try:    
            os.makedirs(p[0])
        except :
            print("mkdir fail：" + p[0])
    print("create: " + localpath)
    try:
        fp = open(localpath,'wb')     #以写模式在本地打开文件
        f.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    except :
        print("create fail: " + localpath)
        f.set_debuglevel(0)         #关闭调试
    try:
        f.close()
        fp.close()     
    except :
        pass

def Pathstr(filepath,isweb): 
    ''' 
    转换文件路径（集团端的文件路径）
    将集团的路径信息转换为本地的路径信息
    isweb0 为输出本地绝对路径，1为服务器文件路径
    '''
    start = filepath
    start = start.find("client")
    fi0 = filepath
    fi0 = fi0[start:]
    if isweb:
        pass
    else:
        fi0 = str(os.getcwd()) + "\\web\\" + fi0
    return fi0
    pass

def KillKingdee():
    ''' 终止金蝶进程 '''
    print("寻找金蝶服务进程...")
    try:
        import psutil
        for x in psutil.pids():
            p = psutil.Process(x)
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
    except :
        print("Kill KingDee Process Fail！")
    
    print("过程完成，进行下一步...")
    pass

def SetKingdeeEnv(drive):
    '''
    设置金蝶的环境变量 drive = 盘符
    drive + r":\Kingdee\eas\client\bin\set-client-env.bat"
    '''
    fp = open(drive + ":/Kingdee/eas/client/bin/set-client-env.bat",'w')
    fp.write("SET EAS_HOME="+ drive + r":\Kingdee\eas" + "\r\n")
    fp.write("SET JAVA_HOME=" + drive + r":\Kingdee\eas\clientjdk" + "\r\n")
    fp.write("SET UPDATE_SERVER=196.168.173.40:6888" + "\r\n")
    fp.write("SET EAS_SERVER=tcp://196.168.173.40:11034" + "\r\n")
    fp.write("SET JVM_INITIAL_HEAPSIZE=64" + "\r\n")
    fp.write("SET JVM_MAX_HEAPSIZE=1024" + "\r\n")
    fp.write("SET ONDEMAND_UPDATE=false" + "\r\n")
    fp.write("SET ISSTART_LOADER=false" + "\r\n")
    fp.write("SET ISMULTI_LOADER=false" + "\r\n")
    fp.write("SET ENABLE_CDN=false" + "\r\n")
    fp.write("SET preheatClient=false" + "\r\n")
    fp.close()
    fp = open(drive + ":/Kingdee/eas/client/bin/set-client-env.bat",'r')
    print (fp.read())
    fp.close()
    pass




kingdee_dir = ''
#查找金蝶目录
if os.path.exists("D:\Kingdee\eas\client"):
    KillKingdee()
    os.system("del /s/f/q D:\Kingdee\eas\client")
    kingdee_dir = "D"
    #下载文件列表
    Downloadfile('filelist.json','D:/Kingdee/eas/filelist.json')
    filelist = []
    filelist_str = open('D:/Kingdee/eas/filelist.json').read()
    #序列化文件列表
    filelist = json.loads(filelist_str)
    for x in filelist:
        Downloadfile(Pathstr(x[0],True),x[0])
        pass

elif os.path.exists("C:\Kingdee\eas\client"):
    KillKingdee()
    os.system("del /s/f/q C:\Kingdee\eas\client")
    kingdee_dir = "C"
    Downloadfile('filelist.json','C:/Kingdee/eas/filelist.json')
    filelist = []
    filelist_str = open('C:/Kingdee/eas/filelist.json').read()
    #序列化文件列表
    filelist = json.loads(filelist_str)
    for x in filelist:
        chengstr = str(x[0])
        chengstr = chengstr.replace("D", "C",1)
        Downloadfile(Pathstr(x[0],True),chengstr)
        pass
    SetKingdeeEnv("C")
else:
    print("非标准金蝶安装方式，不实施更新...")
    

print("\r\n \r\n \r\n \r\n \r\n")
print("更新过程完成，关闭这个窗口即可！")
print("\r\n \r\n \r\n \r\n \r\n")