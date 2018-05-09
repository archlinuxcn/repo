#!/usr/bin/env python3
import re
import requests

resp = requests.get(
    'https://www.dropbox.com/download?plat=lnx.x86_64', allow_redirects=False)
print(re.search(r'(\d+\.4\.\d+)\.tar\.gz', resp.headers['Location']).group(1))
