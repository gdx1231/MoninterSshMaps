# -*- coding: utf-8 -*-
# nas服务器8000端口监控

import os
import time
import moniter_client

if __name__ == '__main__':
    cfg = {
        # 查找本地的进程名称
        'local_progress_name': 'ssh',
        # 查找本地进程的命令行包含的字符
        # ssh -CNfR 44444:127.0.0.1:22 -b 0.0.0.0 root@192.168.1.252
        'local_progress_cmd_tags': ['-CNfR', '44444'],
        # 映射本地端口到远程服务器的命令
        'local_map_cmd': 'ssh -CNfR 44444:127.0.0.1:22 -b 0.0.0.0 root@192.168.1.252 -o TCPKeepAlive=yes',

        # 检查服务器的地址端口与协议，查看是否能正常连接
        'server_chk_addr': '192.168.1.252:44444',
        # 终止服务器已存在的进程的命令
        'server_close_cmd': 'ssh root@192.168.1.252 "python /root/raid/share/guolei/MoninterSshMaps/server_kill.py 44444"'
    }
    while True:
        moniter_client.monitor(cfg)
        time.sleep(10)
