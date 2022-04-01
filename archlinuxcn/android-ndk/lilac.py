from lilaclib import update_pkgver_and_pkgrel, git_pkgbuild_commit, update_aur_repo

def pre_build():
    major_ver, minor_ver = _G.newver.split('.')[:2]
    version_str = f'r{major_ver}'
    if int(minor_ver) > 0:
        version_str += '.' + chr(ord('a') + int(minor_ver))
    update_pkgver_and_pkgrel(version_str)

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
