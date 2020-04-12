from lilaclib import (
    update_pkgver_and_pkgrel,
    git_pkgbuild_commit,
    update_aur_repo,
)


def pre_build():
    update_pkgver_and_pkgrel(_G.newver)


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
