#!/usr/bin/env python

import json
import urllib.request
import re
from pyalpm import vercmp
from functools import cmp_to_key

github_repo = "00-Evan/shattered-pixel-dungeon"
from_pattern = r'(\d+\.\d+\.\d+)([a-z])'
to_pattern = r'\1.\2'
prefix = 'v'

def custom_preproc(vers):
  if len(vers.split('.')) == 3:
    return vers + '.REL'
  else:
    return vers

def remove_prefix(s, prefix):
  if s.startswith(prefix):
    return s[len(prefix):]
  else:
    return s

# Check github tags
# Replace by regex before sorting. This is not currently supported by nvchecker
req = urllib.request.Request('https://api.github.com/repos/{}/tags'.format(github_repo))
body = None
with urllib.request.urlopen(req) as res:
  body = json.load(res)

versions = [ custom_preproc(remove_prefix(re.sub(from_pattern, to_pattern, it['name']), prefix)) for it in body ]
versions.sort(key=cmp_to_key(vercmp))

print(versions[-1])
