#!/usr/bin/env python

import paramiko

ip_addr = '50.76.53.27'

pynet1_port = 7961
pynet2_port = 8022

username = 'pyclass'
password = '88newclass'

ssh_session = paramiko.SSHClient()

ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_session.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=pynet2_port)

stdin, stdout, stderr = ssh_session.exec_command('show version\n')

print stdout.read() 
