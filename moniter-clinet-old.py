# -*- coding: utf-8 -*-

import os
import subprocess
import psutil
import signal
import threading
import time
import socket


def ssh():
    ssh_ids = []
    pid = psutil.pids()
    for k, i in enumerate(pid):
        try:
            proc = psutil.Process(i)
            if proc.name() == 'ssh':
                cmd = ' '.join(proc.cmdline())
                if cmd.find('root@ali2') > 0 and cmd.find('CNfR') > 0:
                    print k, i, proc.name(), proc.exe(), cmd, proc.username()
                    ssh_ids.append(i)

        except psutil.AccessDenied:
            print "psutil.AccessDenied"
        except psutil.NoSuchProcess:
            print "psutil.NoSuchProcess"
        except psutil.TimeoutExpired:
            print "psutil.TimeoutExpired"
    return ssh_ids


def restart():
    ssh_remote_close_all = 'ssh root@ali2.gyap.com.cn "python close_all_ssh.py"'
    print ssh_remote_close_all
    os.system(ssh_remote_close_all)

    ssh_cmd = 'ssh -CNfR 50022:127.0.0.1:22 -b 0.0.0.0 root@ali2.gyap.com.cn -o TCPKeepAlive=yes'
    print ssh_cmd
    os.system(ssh_cmd)


def check_port():
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(2)
        sk.connect(('ali2.gyap.com.cn', 50022))
        ret_bytes = sk.recv(1024)
        sk.close
        ret_str = str(ret_bytes)
        print(ret_str)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        tt = "check port success!"
        print now, 50022, tt
        return True
    except socket.error:
        print socket.error
        return False


def main():
    ssh_ids = ssh()
    print len(ssh_ids)
    if len(ssh_ids) == 0:
        restart()
    else:
        if(check_port()):
            ping_cmd = 'ssh -p 50022 admin@ali2.gyap.com.cn ls'
            print ping_cmd
            rst = os.popen(ping_cmd)
            print '*' * 50
            print rst.read()
        else:
            for pid in ssh_ids:
                print 'KILL ', pid
                os.kill(pid, signal.SIGKILL)
            restart()


while True:
    main()
    time.sleep(10)
# rewrite ".*" https://www.gyap.org;
