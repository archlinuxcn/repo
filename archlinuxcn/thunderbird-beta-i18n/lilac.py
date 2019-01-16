import pathlib
import sys

from lilaclib import git_pkgbuild_commit, update_aur_repo

sys.path.append(str(pathlib.Path(__file__).resolve().parent))  # noqa
import gen_pkgbuild


def pre_build():
    gen_pkgbuild.main(_G.newver)  # noqa


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
