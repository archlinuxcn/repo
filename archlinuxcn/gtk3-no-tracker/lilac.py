from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gtk3')

  packaging = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgbase='):
      line = 'pkgbase=gtk3-no-tracker'
    elif line.startswith('pkgname='):
      line = 'pkgname=(gtk3-no-tracker)'
    elif 'tracker3=true' in line:
      line = line.replace('=true', '=false')
    elif 'tracker3' in line:
      line = line.replace('tracker3', '')
    elif 'gtk_doc=true' in line:
      line = line.replace('=true', '=false')
    elif line.startswith('package_gtk3()'):
      line = 'package_gtk3-no-tracker() {'
      packaging = True
    elif packaging and 'provides=' in line:
      line = line.replace(')', ' gtk3=$pkgver)')
    elif packaging and 'conflicts=' in line:
      line = line.replace(')', ' gtk3)')
    elif packaging and '_pick docs' in line:
      continue
    elif packaging and line == '}':
      packaging = False

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
