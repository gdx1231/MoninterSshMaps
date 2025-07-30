# -*- coding: utf-8 -*-
# nas服务器55022端口监控

import os
import time
import moniter_client

if __name__ == '__main__':
    cfg = {
        # 映射本地端口到远程服务器的命令
        'local_map_cmd': 'ssh -CNfgR 55022:127.0.0.1:22 root@1.gdx.gdx -o TCPKeepAlive=yes',
       # 查找本地的进程名称
        'local_progress_name': 'ssh',
        # 查找本地进程的命令行包含的字符
        'local_progress_cmd_tags': ['-CNfgR', '55022'],
     
        # 检查服务器的地址端口与协议，查看是否能正常连接
        'server_chk_addr': '1.gdx.gdx:55022',
        # 终止服务器已存在的进程的命令/root/kill55022.sh，代码如下：
        # netstat -anltp|grep 55022|grep 0.0.0.0|awk '{print $7}'| cut -d'/' -f1|xargs kill -9
        'server_close_cmd': 'ssh root@1.gdx.gdx "/root/kill55022.sh"'
    }
    while True:
        moniter_client.monitor(cfg)
        # 休眠100秒
        time.sleep(100)
        # 如果是crontab执行，则退出循环
        # break
