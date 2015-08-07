from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config_file.txt")

crypto_map = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group5")

for i in crypto_map:
  print i.text
  for child in i.children:
    print child.text
