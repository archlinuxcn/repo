from lilaclib import *

def pre_build():
  mwver = _G.newvers[1]

  for line in edit_file('PKGBUILD'):
    if line.startswith('_basever='):
      line = f'_basever={mwver}'
    print(line)

  for line in edit_file('lilac.yaml'):
    if 'branch: REL' in line:
      line = f'{line.split(":")[0]} REL{mwver.replace(".", "_")}'
    print(line)

  vcs_update()

def post_build():
  git_add_files(['PKGBUILD', 'lilac.yaml'])
  git_commit()

