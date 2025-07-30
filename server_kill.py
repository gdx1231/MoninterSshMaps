import get_netconn_pids
import os
import sys
import signal

def find_and_key(check_port):
    """
    查找并杀死监听指定端口的进程
    
    参数:
        check_port (int): 需要检查并杀死进程的端口号
    """
    # 获取监听指定端口的进程ID列表
    pids = get_netconn_pids.get_listen_pids(check_port)
    for pid in pids:
        print 'KILL ', pid
        # 发送SIGKILL信号强制终止进程
        os.kill(pid, signal.SIGKILL)
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'USAGE: server_kill.py checkport'
        sys.exit(0)
    check_port = int(str(sys.argv[1]))
    find_and_key(check_port)