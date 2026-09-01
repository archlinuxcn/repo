#!/usr/bin/env python3

from lilaclib import *
import re


def _web3_geth_ver(pkgver: str) -> str:
    tag = f'v{pkgver}'
    r = s.get(
        f'https://raw.githubusercontent.com/ethereum/web3.py/{tag}/'
        'tests/integration/go_ethereum/conftest.py'
    )
    r.raise_for_status()
    m = re.search(
        r'GETH_FIXTURE_ZIP\s*=\s*"geth-([\d.]+)-fixture\.zip"', r.text
    )
    if not m:
        raise RuntimeError(f'GETH_FIXTURE_ZIP not found in web3.py {tag}')
    return m.group(1)


def _geth_commit(geth_ver: str) -> str:
    # 8-char prefix matches gethstore filename: geth-linux-amd64-<ver>-<commit>.tar.gz
    r = s.get(
        f'https://api.github.com/repos/ethereum/go-ethereum/commits/v{geth_ver}'
    )
    r.raise_for_status()
    return r.json()['sha'][:8]


def pre_build():
    geth_ver = _web3_geth_ver(_G.newver)
    geth_commit = _geth_commit(geth_ver)
    for line in edit_file('PKGBUILD'):
        if line.startswith('_geth_ver='):
            line = f'_geth_ver={geth_ver}'
        elif line.startswith('_geth_commit='):
            line = f'_geth_commit={geth_commit}'
        print(line)
    update_pkgver_and_pkgrel(_G.newver)
