import re
from lilaclib import (
    _G, update_pkgver_and_pkgrel, edit_file,
    git_add_files, git_commit,
)

qt_re = re.compile(r"'qt6-base=[^']+'")

def pre_build():
    qt_ver = _G.newvers[2].split('-')[0]
    update_pkgver_and_pkgrel(_G.newver.lstrip('v').lstrip())
    for line in edit_file('PKGBUILD'):
        if 'qt6-base' in line:
            line = qt_re.sub(f"'qt6-base={qt_ver}'", line)
        print(line)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
