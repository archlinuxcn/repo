#!/usr/bin/env python3
from lilaclib import *


def pre_build():
  aur_pre_build(maintainers=['the-k'])

  in_check = False
  depth = 0
  for line in edit_file('PKGBUILD'):
    if not in_check and line.startswith('check()'):
      in_check = True
      depth = line.count('{') - line.count('}')
      continue

    if in_check:
      depth += line.count('{') - line.count('}')
      if depth <= 0:
        in_check = False
      continue

    print(line)
