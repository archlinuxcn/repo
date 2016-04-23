#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

import json
import urllib.request
from functools import cmp_to_key

import pyalpm
from lilaclib import *

build_prefix = 'extra-x86_64'


GITHUB_MAX_TAG = 'https://api.github.com/repos/%s/tags'

def get_version():
    url = GITHUB_MAX_TAG  % "atom/atom"
    headers = {'Accept': "application/vnd.github.quicksilver-preview+json"}
    request = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(request)
    data = json.loads(res.read().decode("utf-8"))
    data = [tag["name"] for tag in data if "-beta" not in tag["name"]] # strip beta release
    data.sort(key=cmp_to_key(pyalpm.vercmp))
    version = data[-1] # get v1.7.2
    return version[1:] # return 1.7.2

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.startswith("pkgver="):
            line="pkgver=" + get_version()
        print(line)
    run_cmd(["updpkgsums"])


def post_build():
    git_add_files(['PKGBUILD'])
    git_commit()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
    #print(get_version())
    single_main(build_prefix)
