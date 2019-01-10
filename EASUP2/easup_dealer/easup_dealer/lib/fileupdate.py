

import os,shutil,hashlib,json
import conf,ftpc


#列出需要更新的文件
def ListUpdateFile():
    updatelist = []
    for x in downfile:
        if IsFileHash(x):
            #文件正确，不执行操作
            print("正解，不处理：" + str(x[0]))
            pass
        else:
            #文件不存在或不正确
            #print("加入更新列表：" + str(x[0]))
            updatelist.append(x)
            pass
    return updatelist
    pass

'''
转换文件路径（集团端的文件路径）
将集团的路径信息转换为本地的路径信息
isweb0 为输出本地绝对路径，1为服务器文件路径
'''
def Pathstr(filepath,isweb):    
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



#判断文件是否需要更新,匹对为真
def IsFileHash(fileinfo):
    re = False

    #计算要被扫描的文件绝对路径
    start = str(fileinfo[0])
    start = start.find("client")
    fi0 = fileinfo[0]
    fi0 = fi0[start:]
    fi0 = str(os.getcwd())+ "\\web\\" + fi0
 
    #查找文件是否在本机存在
    if os.path.exists(fi0):
        #文件存在
        if get_file_md5(fi0) == fileinfo[1]:
            #print("md5匹对")
            re = True
        else:
            print("FileHash False: " + str(fileinfo))
            #print("实际值：" + get_file_md5(fi0))
            pass

        pass
    else:
        #print("这个文件不存在:" + fi0)
        pass
    return re
    pass

#获取文件hash,文件路径返回hash
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
    return hash_value

#清空web目录下的金蝶文件
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


#实施更新
def updatefile():
    notupdatefile = []
    downloadfile = []
    ftpc.Downloadfile('filelist.json','web\\filelist.json')
    print("Loading File List Data ...")
    filelistjson = open('web\\filelist.json').read()
    #序列化文件列表
    downfile = json.loads(filelistjson)
    print("update file:")
    #遍历服务器文件列表数据。
    text_i = 0
    for x in downfile:
        #判断文件是否需要更新，0为需要更新
        text_i = text_i + 1
        if IsFileHash(x):
            notupdatefile.append(x)
        else:
            #开始下载文件
            test = Pathstr(x[0],False)
            ftpc.Downloadfile(Pathstr(x[0],True),Pathstr(x[0],False))
            downloadfile.append(Pathstr(x[0],False))
        pass
    re = []
    re.append(notupdatefile)
    re.append(downloadfile)
    return re
    pass