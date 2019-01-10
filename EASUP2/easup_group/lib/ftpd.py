




from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import conf
print("加载ftpd模块...")

#实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()
print("实例化权限文件分发权限，具体参数请参考 conf.py")
#添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限)
authorizer.add_user(conf.ftpd_user,conf.ftpd_pwd,conf.ftpd_dir, perm=str(conf.ftpd_perm))
#初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer((conf.ftpd_ip,conf.ftpd_port), handler)
#开始服务
print("启动文件分发服务...")
server.serve_forever()