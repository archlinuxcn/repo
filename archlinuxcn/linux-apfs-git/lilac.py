from lilaclib import git_pkgbuild_commit, update_pkgrel, vcs_update

def pre_build():
    update_pkgrel()
    vcs_update()

def post_build():
    git_pkgbuild_commit()
