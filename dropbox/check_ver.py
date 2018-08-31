#!/usr/bin/env python3
import re
import sys

import requests
import requests_toolbelt.utils.dump

resp = requests.get(
    'https://www.dropbox.com/download?plat=lnx.x86_64', allow_redirects=False)
raw_resp = requests_toolbelt.utils.dump.dump_all(resp).decode('ascii')
print(raw_resp, file=sys.stderr)
print(re.search(r'(\d+\.4\.\d+)\.tar\.gz', resp.headers['Location']).group(1))
