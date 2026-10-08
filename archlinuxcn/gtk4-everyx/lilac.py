import re
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

_PATCHES = [
    'everyx-7dc40511032f3ce20c5465556ee6a5935622ae8a.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/7dc40511032f3ce20c5465556ee6a5935622ae8a.patch',
    'everyx-959c3c4a544792fae29122074251dc366396e454.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/959c3c4a544792fae29122074251dc366396e454.patch',
    'everyx-9e142f9a65fad25bea26e8f9c8da67c492c382a7.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/9e142f9a65fad25bea26e8f9c8da67c492c382a7.patch',
    'everyx-76ec6461552648a0a4f9224d7e5a458c74999319.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/76ec6461552648a0a4f9224d7e5a458c74999319.patch',
    'everyx-fba7287a450f118a56bf3e9cb13c1d4975a6ec5b.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/fba7287a450f118a56bf3e9cb13c1d4975a6ec5b.patch',
    'everyx-6005bdabfdb71939c25da030fcdbf9a50f50ee9c.patch::https://gitlab.gnome.org/everyx/gtk/-/commit/6005bdabfdb71939c25da030fcdbf9a50f50ee9c.patch',
]


def pre_build():
    g.files = download_official_pkgbuild('gtk4')

    state = None
    for line in edit_file('PKGBUILD'):
        s = line.strip()

        if state == 'pkgname':
            if s == ')':
                state = None
            continue
        if state == 'skip':
            if line == '}':
                state = None
            continue
        if state == 'source':
            if s == ')':
                state = None
                for entry in _PATCHES:
                    print(f'  "{entry}"')
                print(line)
                continue
            print(line)
            continue
        if state == 'b2sums':
            if line.rstrip().endswith(')'):
                state = None
                print(line[:-1])
                for _ in _PATCHES:
                    print('        SKIP')
                print(')')
                continue
            print(line)
            continue

        if line.startswith('pkgbase='):
            continue
        if line.startswith('pkgname=('):
            print('pkgname=gtk4-everyx')
            state = 'pkgname'
            continue
        if line.startswith('pkgdesc='):
            print(line[:-1] + ", with everyx's patches\"")
            continue
        if line.startswith('arch='):
            print(line)
            print('provides+=(gtk4=$pkgver)')
            print('conflicts+=(gtk4)')
            continue
        if line.startswith('source=('):
            state = 'source'
            print(line)
            continue
        if line.startswith('b2sums=('):
            state = 'b2sums'
            print(line)
            continue
        if s == 'cd gtk':
            print(line)
            for entry in _PATCHES:
                print(f'  git apply -3 ../{entry.split("::", 1)[0]}')
            continue
        if '-D documentation=true' in line:
            print('    -D build-demos=false')
            print('    -D build-examples=false')
            print('    -D build-tests=false')
            print('    -D build-testsuite=false')
            print('    -D documentation=false')
            print('    -D introspection=enabled')
            continue
        if s.startswith('_pick demo ') or s.startswith('_pick docs '):
            continue
        if line.startswith(('package_gtk4-demos()',
                            'package_gtk4-docs()',
                            'package_gtk-update-icon-cache()')):
            state = 'skip'
            continue
        if line.startswith('package_gtk4()'):
            print('package() {')
            continue
        if s.startswith('provides=(') and not s.startswith('provides+=('):
            print(line.replace('provides=(', 'provides+=(', 1))
            continue
        print(line)

    with open('PKGBUILD') as f:
        content = f.read()
    with open('PKGBUILD', 'w') as f:
        f.write(re.sub(r'\n{3,}', '\n\n', content))


def post_build():
    git_add_files(g.files)
    git_commit()
