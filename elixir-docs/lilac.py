# Trimmed lilac.py
#!/usr/bin/env python3
from lilaclib import *

#build_prefix = 'extra-x86_64'

def _get_new_version():
  new_verion = s.get("https://api.github.com/repos/elixir-lang/elixir/releases").json()[0]
  return new_verion['tag_name'][1:]

def pre_build():
  ver = _get_new_version()
  for l in edit_file('PKGBUILD'):
    if l.startswith('pkgver='):
      l = 'pkgver=' + ver
    print(l)
  run_cmd(["updpkgsums"])

def post_build():
  git_add_files("PKGBUILD")
  git_commit()

#if __name__ == '__main__':
#  single_main()
