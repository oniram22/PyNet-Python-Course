import yaml
import json

sample_list = range(10)
sample_list.append("A String")
sample_list.append({})
sample_list[-1]["vendor"] = "Cisco"
sample_list[-1]["model"] = "2951"

print "Python List: ", sample_list

with open("exercise6.yaml", "w") as f:
  f.write(yaml.dump(sample_list, default_flow_style=False)) 

with open("exercise6.json", "w") as f:
  json.dump(sample_list, f) 
