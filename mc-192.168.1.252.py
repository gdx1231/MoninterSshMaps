# -*- coding: utf-8 -*-
# nas服务器8000端口监控

import os
import time
import moniter_client

if __name__ == '__main__':
    cfg = {
        # 映射本地端口到远程服务器的命令
        'local_map_cmd': 'ssh -CNfR 58000:127.0.0.1:8000 -b 0.0.0.0 root@47.gezz.cn -o TCPKeepAlive=yes',
       # 查找本地的进程名称
        'local_progress_name': 'ssh',
        # 查找本地进程的命令行包含的字符
        'local_progress_cmd_tags': ['-CNfR', '58000'],
     
        # 检查服务器的地址端口与协议，查看是否能正常连接
        'server_chk_addr': '47.gezz.cn:58000:http',
        # 终止服务器已存在的进程的命令
        'server_close_cmd': 'ssh root@47.gezz.cn "python /root/MoninterSshMaps/server_kill.py 58000"'
    }
    while True:
        moniter_client.monitor(cfg)
        time.sleep(10)
