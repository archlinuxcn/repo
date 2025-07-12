#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from lilaclib import *


def pre_build():
    schema_version = _G.newvers[0]
    dt = parsedate_to_datetime(_G.newvers[1]).astimezone(ZoneInfo("Asia/Shanghai"))
    dict_version = dt.strftime("%Y%m%d.%H%M%S")

    # update checksums for schema
    update_pkgver_and_pkgrel(f"{schema_version}+r{dict_version}")
