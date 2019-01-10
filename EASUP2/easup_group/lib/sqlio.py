
# -*- coding: UTF-8 -*-


'''

    所有对数据库操作将通过这里实施。

    日期：2019-1-5   作者：杨主任
    Email： 522703331@qq.com 
    GIT：https://github.com/candys-yang/
    blog：http://varmain.com

'''
import sqlite3
import conf

#清空数据库文件hash
def ClearFileHashSQL():
    print("清空数据库hash记录...")
    sqlconn = sqlite3.connect(conf.python_dir + '\database.db')
    sqlcmd = sqlconn.cursor()
    sqlcmd.execute("DELETE FROM filehash")
    sqlconn.commit()
    sqlconn.close()
    pass

#对比文件hash是否与数据库相匹配
def FileHashIs(filepath,md5,wr):
    #print(filepath + "  " + md5)
    sqlconn = sqlite3.connect(conf.python_dir + '\database.db')
    sqlcmd = sqlconn.cursor()
    sqlread = sqlcmd.execute("select * from filehash where filename = ? and hash = ?",[filepath,md5])
    if len(tuple(sqlread)) == 0 : 
        #print("new file :" + str(filepath) + "    " + str(md5))
        if wr:
            WriteSQL(filepath,md5)
        re = []
        re.append(filepath)
        re.append(md5)
        return(re)
    
    '''
    for x in sqlread:
        re.append(x)
        pass
    print (re)
    '''
    sqlconn.close()

    pass

#写入文件hash到数据库
def WriteSQL(filepath,md5):
    sqlconn = sqlite3.connect(conf.python_dir + '\database.db')
    sqlcmd = sqlconn.cursor()
    sqlcmd.executemany("INSERT INTO filehash VALUES ( ?,? )",[(filepath,md5)])
    sqlconn.commit()
    sqlconn.close()
    pass

#读取完整的hash数据
def FileListOut():
    sqlconn = sqlite3.connect(conf.python_dir + '\database.db')
    sqlcmd = sqlconn.cursor()
    sqlread = sqlcmd.execute("select * from filehash")
    re = []
    for x in sqlread:
        re.append(x)
        pass
    return re
    sqlconn.close()

    pass