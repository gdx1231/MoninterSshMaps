# -*- coding: utf-8 -*-
"""
通过crontab定时调用的SSH端口映射监控脚本

该脚本设计用于通过crontab定时任务来执行，确保SSH反向隧道连接的稳定性。
demo.py不同，该脚本更适合在crontab中定期执行，每次执行都会检查连接状态，
并在必要时重新建立连接。

使用方法：
1. 将脚本添加到crontab中，例如每5分钟执行一次：
   */5 * * * * /usr/bin/python3 /path/to/call_by_crontab.py

2. 确保脚本具有执行权限：
   chmod +x call_by_crontab.py

注意事项：
- 该脚本每次执行只会检查一次连接状态，不会循环执行
- 适合在crontab等定时任务系统中使用
- 需要确保执行环境中有psutil等依赖库
"""

import os
import time
import moniter_client

if __name__ == '__main__':
    # SSH端口映射配置
    cfg = {
        # 映射本地端口到远程服务器的命令
        'local_map_cmd': 'ssh -CNfgR 55022:127.0.0.1:22 root@www.gdxsoft.xyz -o TCPKeepAlive=yes',
       # 查找本地的进程名称
        'local_progress_name': 'ssh',
        # 查找本地进程的命令行包含的字符
        'local_progress_cmd_tags': ['-CNfgR', '55022'],
     
        # 检查服务器的地址端口与协议，查看是否能正常连接
        'server_chk_addr': 'www.gdxsoft.xyz:55022',
        # 终止服务器已存在的进程的命令/root/kill55022.sh，代码如下：
        # netstat -anltp|grep 55022|grep 0.0.0.0|awk '{print $7}'| cut -d'/' -f1|xargs kill -9
        'server_close_cmd': 'ssh root@www.gdxsoft.xyz "/root/kill55022.sh"'
    }
    while True:
        moniter_client.monitor(cfg)
        break
         