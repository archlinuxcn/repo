import re
from lilaclib import (
  update_pkgver_and_pkgrel, edit_file,
  git_add_files, git_commit, s,
)

qt_re = re.compile(r"'qt6-base=[^']+'")

def prepare():
  pkgver = _G.newver.lstrip('v').lstrip()
  url = f'https://github.com/telegramdesktop/tdesktop/releases/download/v{pkgver}/tdesktop-{pkgver}-full.tar.gz'
  r = s.head(url, follow_redirects=False)
  if r.status_code == 404:
    return 'upstream source tarball not available'

def pre_build():
  pkgver = _G.newver.lstrip('v').lstrip()
  qt_ver = _G.newvers[2].split('-')[0]
  update_pkgver_and_pkgrel(pkgver)
  for line in edit_file('PKGBUILD'):
    if 'qt6-base' in line:
      line = qt_re.sub(f"'qt6-base={qt_ver}'", line)
    print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
