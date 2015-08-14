#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT=23
TELNET_TIMEOUT=6

remote_conn = telnetlib.Telnet("50.76.53.27", TELNET_PORT, TELNET_TIMEOUT)

output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
output = remote_conn.write("pyclass" + "\n")

output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
output = remote_conn.write("88newclass" + "\n")

time.sleep(1)

output = remote_conn.read_very_eager()

output = remote_conn.write("sh ip int br" + "\n")
time.sleep(1)
output = remote_conn.read_very_eager()

print output

remote_conn.close()
