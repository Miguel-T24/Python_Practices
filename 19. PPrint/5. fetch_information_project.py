# 5. Write a python program to fetch information about a project.

import json
import pprint
from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/scriptgen/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)