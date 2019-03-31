# -*- coding: utf-8 -*-

import os
import subprocess
import psutil
import signal
import threading
import time
import socket

import check_port
import get_process


def main():
    # 第一步 检查端口是否存活
    chk = '192.168.1.252:44444'
    chk_rst = check_port.check_port(chk)
    if chk_rst:
        print 'OK\n\n\n'
        return

    # 第二步 查找所有符合条件的已经存在的进程并结束它们
    exists_pids = get_process.get_process_ids('ssh', ['-CNfR', '44444'])
    for pid in exists_pids:
        print 'KILL ', pid
        os.kill(pid, signal.SIGKILL)
        
    # 第三步 调用远程服务器，终止已存在的进程
    ssh_remote_close_all = 'ssh root@192.168.1.252 "python /root/raid/share/guolei/MoninterSshMaps/server_kill.py 44444"'
    print ssh_remote_close_all
    os.system(ssh_remote_close_all)

    # 第四步
    ssh_cmd = 'ssh -CNfR 44444:127.0.0.1:22 -b 0.0.0.0 root@192.168.1.252 -o TCPKeepAlive=yes'
    print ssh_cmd
    os.system(ssh_cmd)

while True:
    main()
    time.sleep(10)
