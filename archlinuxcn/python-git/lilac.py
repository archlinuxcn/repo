from lilaclib import git_pkgbuild_commit, update_aur_repo

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
