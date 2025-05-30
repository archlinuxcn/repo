#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from lilaclib import *


def pre_build():
    schema_version = _G.newvers[0]

    for line in edit_file('PKGBUILD'):
        if line.startswith('_schema_version='):
            line = f'_schema_version={schema_version}'
        print(line)
