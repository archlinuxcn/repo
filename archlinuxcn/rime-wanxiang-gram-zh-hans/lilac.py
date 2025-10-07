#!/usr/bin/python3

from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo
from lilaclib import *


def pre_build():
    dt = parsedate_to_datetime(_G.newvers[0])
    pkgver = dt.astimezone(ZoneInfo("Asia/Shanghai")).strftime("%Y%m%d.%H%M%S")

    update_pkgver_and_pkgrel(pkgver)
