#!/usr/bin/python3

from lilac2.api import *
import subprocess
import sys
from pathlib import Path

import requests

# lilac2 API import (available in lilac build environment)
from lilac2.api import edit_file

def fetch_release_body(version: str) -> str:
    """Get the release body from GitHub API."""
    url = f"https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/tags/{version}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    body = data.get("body")
    if not body:
        raise ValueError(f"No release body found for version {version}")
    # Normalise line endings (original script removed CR)
    return body.replace("\r\n", "\n").replace("\r", "\n")


def _update_changelog(version) -> None:
    changelog = Path("changelog.md")

    ver = _G.newver
    release_body = fetch_release_body(ver)

    first = True
    for line in edit_file(str(changelog)):
        if first:
            first = False
            if line != f"## {ver}":
                print(f"## {ver}")
                print()
                for bline in release_body.splitlines():
                    print(bline)
                print()
        print(line)

def pre_build():
    newver = _G.newver.lstrip("GE-Proton").replace('-', '.')
    update_pkgver_and_pkgrel(newver)
    _update_changelog(newver)

def post_build():
    git_pkgbuild_commit()

