# -*- coding: utf-8 -*-
import os
import subprocess
import socket
import time
import sys
from urllib import urlencode
from socket import gethostname

def check_port(addrAndPort):
    """
    检查端口是否可用.

    Args:
        addrAndPort: 地址和端口及协议(http/https请求协议是http)，
        例如 www.baidu.com:80:http
    Returns:
       是否连接成功.
    """
    addr1 = addrAndPort.split(':')
    addr = addr1[0]
    port = int(addr1[1])
    net_type = ''
    if len(addr1) > 2:
        net_type = addr1[2]

    print (addr, port, net_type)
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(2)
        sk.connect((addr, port))
        if port == 80 or port == 443 or net_type == 'http':
            sk.send('GET / HTTP/1.0\r\n\r\n')

        # sk.connect(('127.0.0.1', 22))
        ret_bytes = sk.recv(102)
        sk.close
        ret_str = str(ret_bytes)
        print(ret_str)
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        tt = "check port success!"
        #logfile = "/home/op/check.log"
        #f = open(logfile, 'a+')
        #f.write(now + " " + tt + "\n")
        # f.close()
        print (now, port, tt)
        return True
    except socket.error:
        print (socket.error)
        return False


def check_ports(addrs):
    failed_ports = []
    for addr in addrs:
        isok = check_port(addr)
        if not isok:
            failed_ports.append(addr)
    return failed_ports


if __name__ == '__main__':
    check_ports(['127.0.0.1:22', '192.168.1.252:880:http'])
