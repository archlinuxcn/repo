#!/usr/bin/env python3

from lilaclib import *


def get_caddy_latest_release_tag():
    resp = s.get(
        'https://api.github.com/repos/caddyserver/caddy/releases/latest'
    )
    body = resp.json()
    return body["tag_name"]


def get_caddy_dist_commit_by_tag(tag):
    resp = s.get(
        'https://api.github.com/repos/caddyserver/dist/tags'
    )
    body = resp.json()

    _dist_commit = list(filter(lambda x: x["name"] == tag, body))
    if len(_dist_commit) == 1:
        dist_commit = _dist_commit[0]
        return dist_commit["commit"]["sha"]
    else:
        raise OSError("Not Found {} dist commit".format(tag))


def pre_build():
    caddy_tag = get_caddy_latest_release_tag()
    dist_commit = get_caddy_dist_commit_by_tag(caddy_tag)

    pkgver = caddy_tag.lstrip('v')

    for line in edit_file('PKGBUILD'):
        if line.startswith('_gitcommit='):
            line = '_gitcommit={}'.format(caddy_tag)
        if line.startswith('_distcommit='):
            line = '_distcommit={}'.format(dist_commit)
        print(line)

    update_pkgver_and_pkgrel(pkgver)
