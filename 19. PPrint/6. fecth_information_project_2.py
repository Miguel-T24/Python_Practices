# 6. Write a python program to fectch information about a project. using pprint() function. Limit the result to a certain  level and specify the width of content

import json
import pprint
from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/aioxmpp/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info, depth = 1, width = 160)