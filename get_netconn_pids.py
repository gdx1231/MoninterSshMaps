# -*- coding: utf-8 -*-

import psutil
import sys

def get_listen_pids(checkport):
    """
    获取监听端口对应的程序id

    Args:
        checkport: 检查的端口
    Returns:
        监听的程序id数组.
    """
    net_ids = []
    map_ids ={}
    try:
        conns = psutil.net_connections()
        for cnn in conns: 
            port = cnn.laddr[1]
            status = cnn.status
            
            if status == 'LISTEN' and port == checkport:
                pid = cnn.pid
                if pid not in map_ids:
                    map_ids[pid] =1
                    net_ids.append(pid)
    except psutil.AccessDenied:
         print("psutil.AccessDenied")
    
    return net_ids


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('USAGE: netstats.py checkport')
        sys.exit(0)
    
    check_port = int(str(sys.argv[1]))
    # print check_port
    ids = get_listen_pids(check_port)
    print(ids)
    for id in ids:
        print(id)