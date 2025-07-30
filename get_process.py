# -*- coding: utf-8 -*-

import os
import subprocess
import psutil
import signal
import threading
import time
import socket


def get_process_ids(progressName, listChkTags):
    """
    获取符合表达式的所有进程id，例如命令行
    ssh -CNfR 44444:127.0.0.1:22 -b 0.0.0.0 root@192.168.1.252

    Args:
       progressName 进程的名称
        listChkTags 命令行包含的特征字符串列表，例如：['CNfR','44444']
    Returns:
        符合特征的进程id列表
    """
    ssh_ids = []
    pid = psutil.pids()
    for k, i in enumerate(pid):
        try:
            proc = psutil.Process(i)
            if proc.name() == progressName:
                cmd = ' '.join(proc.cmdline())
                ismatch = True
                for tag in listChkTags:
                    if cmd.find(tag) >= 0:
                        ismatch = ismatch and True
                    else:
                        ismatch = ismatch and False
                if ismatch:
                    print(k, i, proc.name(), proc.exe(), cmd, proc.username())
                    ssh_ids.append(i)
        except psutil.AccessDenied as e:
            print("psutil.AccessDenied")
        except psutil.NoSuchProcess as e:
            print("psutil.NoSuchProcess")
        except psutil.TimeoutExpired as e:
            print("psutil.TimeoutExpired")
    return ssh_ids


if __name__ == '__main__':
    ids = get_process_ids('ssh', ['-CNfR', '44444'])
    print(ids)