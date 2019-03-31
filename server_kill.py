import get_netconn_pids
import os
import sys
import signal

def find_and_key(check_port):
    pids = get_netconn_pids.get_listen_pids(check_port)
    for pid in pids:
        print 'KILL ', pid
        os.kill(pid, signal.SIGKILL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'USAGE: server_kill.py checkport'
        sys.exit(0)
    check_port = int(str(sys.argv[1]))
    find_and_key(check_port)