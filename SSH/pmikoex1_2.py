#!/usr/bin/env python

import paramiko, time
from getpass import getpass

ip = '184.105.247.71'
user = 'pyclass'
password = '88newclass'
port = 22

if __name__ == '__main__':
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, username=user, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.settimeout(8.0)
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('show version\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('\n')
    remote_conn.send('enable\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('configure terminal\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('logging buffered 9000\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('exit\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('show logging\n')
    outp = remote_conn.recv(5000)
    print outp
    remote_conn.send('\n')
    outp = remote_conn.recv(5000)
    print outp
