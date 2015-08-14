#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

ROUTER_IP = "50.76.53.27"
ROUTER1_PORT = "7961"
ROUTER2_PORT = "8061"
OID_SYS_NAME = "1.3.6.1.2.1.1.5.0"
OID_SYS_DESC = "1.3.6.1.2.1.1.1.0"

COMMUNITY_STRING = "galileo"

router1 = (ROUTER_IP, COMMUNITY_STRING, ROUTER1_PORT)
router2 = (ROUTER_IP, COMMUNITY_STRING, ROUTER2_PORT)

snmp_data = snmp_get_oid(router1, oid=OID_SYS_NAME, display_errors=True)
print snmp_extract(snmp_data)

snmp_data = snmp_get_oid(router1, oid=OID_SYS_DESC, display_errors=True)
print snmp_extract(snmp_data)

snmp_data = snmp_get_oid(router2, oid=OID_SYS_NAME, display_errors=True)
print snmp_extract(snmp_data)

snmp_data = snmp_get_oid(router2, oid=OID_SYS_DESC, display_errors=True)
print snmp_extract(snmp_data)
