# -*- coding: utf-8 -*-

import os
import time
import moniter_client

if __name__ == '__main__':
    # 服务器域名参数
    domain = "1.gdx.gdx"
    # 本地和远程端口参数
    local_port = "22"
    remote_port = "55022"
    server_kill_cmd = "netstat -anltp|grep " + remote_port + "|grep 0.0.0.0|awk '{print $7}'| cut -d'/' -f1|xargs kill -9"
    cfg = {
        # 映射本地端口到远程服务器的命令
        'local_map_cmd': 'ssh -CNfgR ' + remote_port + ':127.0.0.1:' + local_port + ' root@' + domain + ' -o TCPKeepAlive=yes',
       # 查找本地的进程名称
        'local_progress_name': 'ssh',
        # 查找本地进程的命令行包含的字符
        'local_progress_cmd_tags': ['-CNfgR', remote_port],
     
        # 检查服务器的地址端口与协议，查看是否能正常连接
        'server_chk_addr': domain + ':' + remote_port,
        # 终止服务器已存在的进程的命令，代码如下：
        # netstat -anltp|grep 55022|grep 0.0.0.0|awk '{print $7}'| cut -d'/' -f1|xargs kill -9
        'server_close_cmd': 'ssh root@' + domain + ' "' + server_kill_cmd + '"'
    }
    
    # 打印配置信息
    for key in cfg:
        print(key+":\r\n\t", cfg[key])
    
    moniter_client.monitor(cfg)
    # break
    # time.sleep(100)