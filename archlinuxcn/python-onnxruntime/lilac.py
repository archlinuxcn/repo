from lilaclib import (
    update_pkgver_and_pkgrel,
    git_pkgbuild_commit,
    update_aur_repo,
    vcs_update,
)


def pre_build():
    # git repos are not updated by default as lilac uses --holdver
    vcs_update()
    update_pkgver_and_pkgrel(_G.newver)


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
