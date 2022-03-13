from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('nvidia')
  for line in edit_file('PKGBUILD'):
    if 'pkgname=' in line:
      line = 'pkgname=nvidia-mainline'
    elif 'linux-headers' in line:
      line = line.replace('linux-headers', 'linux-mainline-headers')
    elif '_kernver' in line:
      line = line.replace('linux', 'linux-mainline')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
