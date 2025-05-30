#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from lilaclib import *


def pre_build():
    schema_version = _G.newvers[0]

    for line in edit_file('PKGBUILD'):
        if line.startswith('_schema_version='):
            line = f'_schema_version={schema_version}'
        print(line)

    # update checksums for schema
    update_pkgver_and_pkgrel(schema_version)

    for line in edit_file('PKGBUILD'):
        if line.startswith('b2sums=('):
            line = "b2sums=('SKIP'"
        print(line)

    vcs_update()