#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from lilaclib import *


def pre_build():
    schema_version = _G.newvers[0]
    dict_version = parsedate_to_datetime(_G.newvers[1]).astimezone(ZoneInfo("Asia/Shanghai"))

    # update checksums for schema
    update_pkgver_and_pkgrel(f"{schema_version}+r{dict_version}")
