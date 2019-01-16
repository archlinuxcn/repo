from lilaclib import *

def pre_build():
  pypi_pre_build(depends=['python-psutil'])
  for line in edit_file('PKGBUILD'):
    if line.startswith('_pkgname'):
      print('_pkgname=memory_profiler')
    else:
      print(line)

def post_build():
  pypi_post_build()
  update_aur_repo()
