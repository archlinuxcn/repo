from lilaclib import *

def get_latest_release_tag_from_github(repo_name: str):
    resp = s.get(
        'https://api.github.com/repos/{}/releases/latest'.format(repo_name)
    )
    body = resp.json()
    return body['tag_name']

def pre_build():
    latest_tag = get_latest_release_tag_from_github('ooni/probe-cli')
    _pkgver = latest_tag.lstrip('v')
    pkgver = _pkgver

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgver'):
            line = '_pkgver={}'.format(_pkgver)
        print(line)
    
    update_pkgver_and_pkgrel(pkgver, updpkgsums=True)

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
