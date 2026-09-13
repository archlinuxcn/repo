#!/usr/bin/env python3

from lilaclib import *


def _update_globalhotkeys_submodule():
    # 更新 GlobalHotKeys commit
    newver = _G.newver
    url = f'https://api.github.com/repos/2dust/v2rayN/contents/v2rayN/GlobalHotKeys?ref={newver}'
    resp = s.get(url, timeout=60)
    resp.raise_for_status()
    sha = resp.json()['sha']

    for line in edit_file('PKGBUILD'):
        if line.startswith('_ghk_commit='):
            line = f'_ghk_commit={sha}'
        print(line)


def pre_build():
    _update_globalhotkeys_submodule()
    update_pkgver_and_pkgrel(_G.newver)


def post_build():
    git_pkgbuild_commit()
