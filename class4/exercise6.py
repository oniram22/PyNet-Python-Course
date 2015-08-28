#!/usr/bin/env python

from netmiko import ConnectHandler

pynet2 = {
  'device_type': 'cisco_ios',
  'ip': '50.76.53.27',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 8022
}

pynet2_session = ConnectHandler(**pynet2)

print pynet2_session.send_command('show arp')
