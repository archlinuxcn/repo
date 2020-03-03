# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    _pkgver = requests.get('https://papermc.io/api/v1/paper').json().get('versions')[0]
    _build = requests.get('https://papermc.io/api/v1/paper' + '/' + _pkgver).json().get('builds').get('latest')
    with open('PKGBUILD') as f:
        pkgbuild = f.read()
    pkgbuild=re.sub(r'''(?<=^_pkgver=)['"]?([\d.]+)['"]?''', _pkgver, pkgbuild, count=1, flags=re.MULTILINE)
    pkgbuild=re.sub(r'''(?<=^_build=)['"]?([\d.]+)['"]?''', _build, pkgbuild, count=1, flags=re.MULTILINE)
    with open('PKGBUILD', 'w') as f:
        f.write(pkgbuild)
    run_cmd(['updpkgsums'])

