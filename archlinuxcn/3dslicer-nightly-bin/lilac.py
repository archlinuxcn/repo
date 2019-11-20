#!/usr/bin/env python3

from lilaclib import *
from nvchecker.get_version import get_version
import asyncio


def pre_build():
    version_conf = {'url': 'https://download.slicer.org',
                    'regex': 'version (\d+.\d+.\d+)'}
    revision_conf = {'url': 'https://download.slicer.org',
                     'regex': 'revision (\d+.\d+.\d+)'}
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    version = loop.run_until_complete(get_version(name='3dslicer-nightly-bin', conf=version_conf))
    revision = loop.run_until_complete(get_version(name='3dslicer-nightly-bin', conf=revision_conf))
    loop.close()
    newver = version + '.r' + revision
    update_pkgver_and_pkgrel(newver)


def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

# vim:set ts=2 sw=2 et:
