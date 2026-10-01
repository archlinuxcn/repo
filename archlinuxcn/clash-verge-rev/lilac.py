#!/usr/bin/python3

from lilaclib import *
from urllib.request import urlopen
import tomllib

def pre_build():
    update_pkgver_and_pkgrel(_G.newver)

    with urlopen(f"https://raw.githubusercontent.com/clash-verge-rev/clash-verge-rev/v{_G.newver}/src-tauri/Cargo.toml") as response:
        config = tomllib.loads(response.read().decode())

    ipc_ver = config['dependencies']['clash_verge_service_ipc']['version']

    for line in edit_file('PKGBUILD'):
        if line.startswith('_ipc_ver='):
            line = f"_ipc_ver={ipc_ver}"

        print(line)

    run_protected(['updpkgsums'])
