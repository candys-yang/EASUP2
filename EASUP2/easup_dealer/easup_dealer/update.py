
import os,shutil,hashlib,json,sys
import configparser
import conf
sys.path.append(conf.python_dir + "/lib")
import ftpc
import fileupdate
import time
while True:
    print("policy.txt copying...")
    #ftpc.Downloadfile('policy.txt','web\\policy.txt')
    policystr = open('web\\policy.txt')
    config = configparser.ConfigParser()
    config.readfp(policystr)
    cur_h = int(time.strftime("%H"))
    s_h = int(config.get("dealer","dealer_update_time_start"))
    e_h = int( config.get("dealer","dealer_update_time_stop"))
    #判断是否符合策略！符合则更新。
    if cur_h >= s_h and e_h >= cur_h:
        print("开始更新任务...")
        fileupdate.updatefile()
        pass
    else:
        print("根据策略任务，跳过更新过程，等待下一次时间节点。")

    print("更新过程完成，休眠...")
    time.sleep(3000)    #每次检查更新的休眠时间长度（s）
    pass



