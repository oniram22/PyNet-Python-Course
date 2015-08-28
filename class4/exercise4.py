#!/usr/bin/env python

import pexpect 

ip_addr = '50.76.53.27'

pynet1_port = 7961
pynet2_port = 8022

username = 'pyclass'
password = '88newclass'

cli = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, pynet2_port))

cli.timeout = 3

cli.sendline("yes")
cli.expect("ssword:")
cli.sendline(password)
cli.expect("#")
cli.sendline("conf t")
cli.expect("#")
cli.sendline("logging buffered 4097")
cli.expect("#")
cli.sendline("end")
cli.expect("#")
cli.sendline("show run | inc logging buffered")
cli.expect("#")
print cli.before
