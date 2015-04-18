from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('wireshark-gtk')

  packaging = False
  ignoring = False
  for line in edit_file('PKGBUILD'):
    if ignoring:
      if line.strip() == '}':
        ignoring = False
        packaging = False
      continue

    if line.startswith('pkgname='):
      line = 'pkgname=wireshark-gtk2'
    elif line.startswith('makedepends=('):
      line = line.replace("'qt4' 'gtk3'", "'gtk2'")
    elif '--with-qt' in line:
      continue
    elif '--with-gtk3' in line:
      line = '      --with-gtk2 \\'
    elif line.startswith('package_wireshark-cli('):
      ignoring = True
      continue
    elif line.startswith('package_wireshark-qt('):
      ignoring = True
      continue
    elif line.startswith('package_wireshark-gtk('):
      line = 'package() {'
      packaging = True
    elif packaging:
      if 'GTK frontend' in line:
        line = line.replace('GTK', 'GTK 2')
      elif line.strip().startswith('depends='):
        line = line.replace('gtk3', 'gtk2')
      elif line.strip().startswith('replaces='):
        continue
      elif line.strip().startswith('conflicts='):
        line = '  conflicts=(wireshark-gtk)'

    print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  single_main()
