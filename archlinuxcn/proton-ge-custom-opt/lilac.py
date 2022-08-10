from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  
  aur_pre_build(maintainers=['loathingkernel'])
  
  for line in edit_file('PKGBUILD'):
    if 'nocona' in line:
      line = line.replace('nocona', 'x86-64-v3')
    elif 'core-avx2' in line:
      line = line.replace('core-avx2', 'generic')
    elif '-C opt-level=2' in line:
      line = line.replace('-C opt-level=2', '-C opt-level=3')
    elif line.startswith('pkgname='):
      line = 'pkgname=proton-ge-custom-opt\n_pkgname=proton-ge-custom'
    elif r'${pkgname}' in line:
      line = line.replace(r'${pkgname}', r'${_pkgname}')

    print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
