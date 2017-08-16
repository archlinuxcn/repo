#!/usr/bin/python3
from lilaclib import *
import datetime
import fileinput
import re

build_prefix = 'extra-x86_64'


def _get_new_version():
    web = s.head(
        "https://download.mozilla.org/?product=firefox-nightly-latest-l10n-ssl&os=linux64&lang=zh-CN").headers['Location']
    return re.search(r'(\d{2})\.(\d\w\d*)', web).group()


def _today():
    return datetime.datetime.strftime(datetime.date.today(), "%Y%m%d")


def pre_build():
    ver = _get_new_version()
    date = _today()
    today_ver = '_'.join([ver, date])
    with fileinput.input(files=('PKGBUILD'), inplace=1) as f:
        for l in f:
            l = l.rstrip('\n')
            if l.startswith('pkgver='):
                l = 'pkgver=' + today_ver
            print(l)
    run_cmd(['updpkgsums'])


def post_build():
    # do something after successful build
    git_add_files('PKGBUILD')
    git_commit()


if __name__ == '__main__':
    single_main()
