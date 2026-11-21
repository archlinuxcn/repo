#!/usr/bin/python3

from lilaclib import *
from urllib.request import urlopen
import json

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)

    with urlopen(f"https://raw.githubusercontent.com/litocpp/lito/v{_G.newver}/deps.json") as response:
        deps = json.load(response)

    rstd_commit = deps["rstd"]["rev"]
    luato_commit = deps["luato"]["rev"]
    licrypto_commit = deps["licrypto"]["rev"]
    ligraph_commit = deps["ligraph"]["rev"]
    liresto_commit = deps["liresto"]["rev"]

    for line in edit_file('PKGBUILD'):
        if line.startswith('_rstd_commit='):
            line = f"_rstd_commit={rstd_commit}"
        elif line.startswith('_luato_commit='):
            line = f"_luato_commit={luato_commit}"
        elif line.startswith('_licrypto_commit='):
            line = f"_licrypto_commit={licrypto_commit}"
        elif line.startswith('_ligraph_commit='):
            line = f"_ligraph_commit={ligraph_commit}"
        elif line.startswith('_liresto_commit='):
            line = f"_liresto_commit={liresto_commit}"

        print(line)

    run_protected(['updpkgsums'])
