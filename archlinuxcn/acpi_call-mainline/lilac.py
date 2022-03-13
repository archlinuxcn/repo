from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('acpi_call')
  for line in edit_file('PKGBUILD'):
    if 'pkgname=' in line:
      line = 'pkgname=acpi_call-mainline'
    elif 'depends' in line:
      line = line.replace('linux', 'linux-mainline')
    elif '_kernver' in line:
      line = line.replace('linux', 'linux-mainline')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
