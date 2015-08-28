#!/usr/bin/env python

import paramiko
import time

ip_addr = '50.76.53.27'

pynet1_port = 7961
pynet2_port = 8022

username = 'pyclass'
password = '88newclass'

ssh_session = paramiko.SSHClient()

ssh_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_session.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=pynet2_port)

cli = ssh_session.invoke_shell()

cli.recv(5000)
cli.send("conf t\n")
cli.recv(5000)
cli.send("logging buffered 1111\n")
cli.recv(5000)
cli.send("end\n")
cli.recv(5000)
cli.send("show run | include logging buffered\n")
time.sleep(5)
output = cli.recv(5000)
print output 
