#!/usr/bin/python3

from email.utils import parsedate_to_datetime
import time

def pre_build():
    date_object = parsedate_to_datetime(_G.newver)
    timestamp = int(time.mktime(date_object.timetuple()))
    pkgver = f"lts.{timestamp}"

    update_pkgver_and_pkgrel(pkgver)
