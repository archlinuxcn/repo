from urllib.request import urlopen

from lilaclib import *

# 本地测试用
# from types import SimpleNamespace
# _G = SimpleNamespace(newver='v0.1.47')


def pre_build():
    version = _G.newver
    url = f"https://raw.githubusercontent.com/jswysnemc/mark-shot/{version}/packaging/aur/PKGBUILD"
    with urlopen(url) as r:
        pkgbuild = r.read().decode("utf-8")
    with open("PKGBUILD", "w") as f:
        f.write(pkgbuild)


def post_build():
    git_add_files(["PKGBUILD"])
    git_commit()
