#!/usr/bin/python3
import sys
import urllib

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   html = response.read()
   #status = response.sta

print("Body response:")
print(f"    - type: {type(html)}")
print(f"    - content: {html}")
print(f"    - utf8 content: {html.decode('utf-8')}")