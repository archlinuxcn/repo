#!/usr/bin/env python

import json
import urllib.request
import re
from pyalpm import vercmp
from functools import cmp_to_key

github_repo = "yairm210/Unciv"
from_pattern = r'(.*)-patch(\d+)'
to_pattern = r'\1.\2'
prefix = ''

def custom_preproc(vers):
  # Sometimes, vers contains a `-XXX` suffix
  # that is not covered by `from_pattern`.
  if "-" in vers:
    vers = vers.replace('-', '.')
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
req = urllib.request.Request('https://api.github.com/repos/{}/releases'.format(github_repo))
body = None
with urllib.request.urlopen(req) as res:
  body = json.load(res)

versions = [ custom_preproc(remove_prefix(re.sub(from_pattern, to_pattern, it['tag_name']), prefix)) for it in body if it['prerelease'] != True ]
versions.sort(key=cmp_to_key(vercmp))

print(versions[-1])
