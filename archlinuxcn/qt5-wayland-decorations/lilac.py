#!/usr/bin/env python3

import re
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()


def get_patches_after_marker(content, marker):
    lines = content.split("\n")
    found_marker = False
    patches = []

    for line in lines:
        line = line.strip()

        if not line:  # 跳过空行
            continue

        if line == marker:
            found_marker = True
            continue

        if found_marker:
            if line.startswith("#"):  # 遇到下一个注释，停止收集
                break
            if line.startswith("Patch"):  # 收集 Patch 行
                patches.append(line)

    return patches


def pre_build():
    # _G = SimpleNamespace(
    #     {
    #         "newvers": ["5.15.18+kde+r55", "5bfde592e677861db0519f042fc9f2941b78dcde"],
    #     }
    # )
    [version, patch_commit] = _G.newvers

    # 获取 fedora QAdwaitaDecorations patchs
    patchs_base_url = (
        f"https://src.fedoraproject.org/rpms/qt5-qtwayland/raw/{patch_commit}/f"
    )
    url = f"{patchs_base_url}/qt5-qtwayland.spec"
    r = s.get(url)
    r.raise_for_status()
    spec = r.content.decode()
    patche_lines = get_patches_after_marker(
        spec, "# Use QAdwaitaDecorations by default"
    )
    patche_sources = [
        f"{patch.split(':')[0]}-{patch_commit}.patch::{patchs_base_url}/{patch.split(':')[1].strip()}"
        for patch in patche_lines
    ]

    # 修改 PKGBUILD
    g.files = download_official_pkgbuild("qt5-wayland")

    # 从 PKGBUILD 文件中获取源码目录
    with open("PKGBUILD", "r", encoding="utf-8") as f:
        pkgbuild_content = f.read()

    match = re.search(r"source=\(([^:]+)::", pkgbuild_content)
    src_dir = match and match.group(1) or ""

    state = "out"
    for line in edit_file("PKGBUILD"):
        if line.startswith("# Maintainer:"):
            line = "# Maintainer: Gavin Luo <lunt.luo@gmail.com>\n" + line.replace(
                "Maintainer:", "Contributor:"
            )

        elif line.startswith("pkgname="):
            line = f"_pkgname={line.split('=')[1]}\n" + f"{line}-decorations"

        elif line.startswith("pkgdesc="):
            line = re.sub(r"'$", " - using QAdwaitaDecorations'", line)

        elif line.startswith("groups=("):
            line = f"provides=('qt5-wayland={version}')\n" + "conflicts=('qt5-wayland')"

        elif line.startswith("_pkgfqn="):
            line = line.replace("pkgname", "_pkgname")

        elif line.startswith("source=("):
            line = re.sub(
                r"\)$", "\n        " + "\n        ".join(patche_sources) + ")", line
            )

        elif line.startswith("prepare("):
            state = "prepare"
        elif state == "prepare" and line.endswith("}"):
            line = (
                f"\n  cd {src_dir}"
                + """
  # Use QAdwaitaDecorations by default
  for patch_file in ${srcdir}/*.patch; do
    patch -p1 -i "$patch_file"
  done
"""
                + line
            )
            state = "out"

        print(line)

    update_pkgver_and_pkgrel(version)


def post_build():
    git_pkgbuild_commit()
