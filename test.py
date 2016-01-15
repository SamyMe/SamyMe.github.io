import yaml
from jinja2 import Template


f = open('data.yml')
dataMap = yaml.safe_load(f)
f.close()

print dataMap
