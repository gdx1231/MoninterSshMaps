# -*- coding: utf-8 -*-
import os
import subprocess
import socket
import time
import sys
from urllib import urlencode
from socket import gethostname


def check_port():
    port = [50022]
    failed_port = []
    for _each_port in port:
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(2)
            sk.connect(('ali2.gyap.com.cn', _each_port))
            # sk.connect(('127.0.0.1', 22))
            ret_bytes = sk.recv(1024)
            sk.close
            ret_str = str(ret_bytes)
            print(ret_str)
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            tt = "check port success!"
            #logfile = "/home/op/check.log"
            #f = open(logfile, 'a+')
            #f.write(now + " " + tt + "\n")
            #f.close()
            print now, _each_port, tt
        except socket.error:
            failed_port.append(_each_port)

    for _each_port in failed_port:
        print _each_port
        


if __name__ == '__main__':
    check_port()
