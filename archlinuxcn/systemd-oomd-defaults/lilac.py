#!/usr/bin/env python3
from lilaclib import *

import shutil
import os
import re

# from types import SimpleNamespace
# _G = SimpleNamespace(
#     {
#         "newver": "399885597ce9f7cc63673c3369086021f0b01176",
#     }
# )
repo_dir = "systemd"
repo_url = "https://src.fedoraproject.org/rpms/systemd.git"


def update_pkg():
    if not os.path.isdir(repo_dir):
        os.mkdir(repo_dir)
        run_cmd(["git", "clone", repo_url, repo_dir], use_pty=True)
    else:
        with at_dir(repo_dir):
            run_cmd(["git", "reset", "--hard"])
            git_pull()

    reversion = None
    with at_dir(repo_dir):
        reversion = run_cmd(["git", "rev-list", "--count", _G.newver]).strip()

    if not reversion:
        raise Exception("Failed to get revision")

    for line in edit_file("PKGBUILD"):
        if line.startswith("_revision="):
            line = f"_revision={reversion}"
        print(line)


def pre_build():
    sums_before = obtain_array("sha256sums")

    shutil.copy("PKGBUILD", "PKGBUILD.backup")

    for line in edit_file("PKGBUILD"):
        if line.startswith("_commit="):
            line = f"_commit={_G.newver}"
        print(line)

    run_cmd(["updpkgsums"])

    state = "out"
    for line in edit_file("PKGBUILD"):
        if line.startswith("sha256sums=("):
            state = "prepare"
        elif state == "prepare" and line.endswith(")"):
            line = re.sub(r"\w+", "SKIP", line)
            state = "out"

        print(line)

    sums_after = obtain_array("sha256sums")

    if sums_before == sums_after:
        shutil.move("PKGBUILD.backup", "PKGBUILD")
        return
    else:
        update_pkg()

    os.remove("PKGBUILD.backup")


def post_build():
    git_pkgbuild_commit()
