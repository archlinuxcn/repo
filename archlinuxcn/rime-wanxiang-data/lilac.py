#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
import re
from lilaclib import *

def pre_build():
    old_schema_versions = None
    for line in open('PKGBUILD').readlines():
        if line.startswith('_schema_version='):
            old_schema_versions = line.split('=')[1].strip()

    print(_G.on_build_vers)
    schema_version = _G.on_build_vers[0][1]

    if not re.match(r'^\d+[\.\d]*\d+$', schema_version):
        schema_version=old_schema_versions
        print(f'invalid schema version from on_build_vers: [{schema_version}]')

    for line in edit_file('PKGBUILD'):
        if line.startswith('_schema_version='):
            line = f'_schema_version={schema_version}'
        print(line)

    dt = parsedate_to_datetime(_G.newver)
    dict_version = dt.astimezone(ZoneInfo("Asia/Shanghai")).strftime("%Y%m%d")

    pkgver = f'{schema_version}+{dict_version}'
    update_pkgver_and_pkgrel(pkgver)
