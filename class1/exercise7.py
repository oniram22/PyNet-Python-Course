import yaml
import json

with open("exercise6.yaml") as f:
  sample_list = yaml.load(f)

print "YAML: ", sample_list 

with open("exercise6.json") as f:
  sample_list = json.load(f) 

print "JSON: ", sample_list
