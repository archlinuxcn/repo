#!/usr/bin/env python3

import importlib.util
import os
import shutil
import sys
import tarfile
import tempfile

from lilaclib import *
from operator import itemgetter


def get_latest_release_tag_from_github(repo_name: str):
    resp = s.get(
        'https://api.github.com/repos/{}/releases/latest'.format(repo_name)
    )
    body = resp.json()
    return body['tag_name']


def import_module_from_path(module_name: str, file_path: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def get_naiveproxy_latest_release_tag():
    return get_latest_release_tag_from_github('klzgrad/naiveproxy')


def download_and_extract_source():
    latest_tag = get_naiveproxy_latest_release_tag()
    latest_tar_gz_url = 'https://github.com/klzgrad/naiveproxy/archive/refs/tags/{}.tar.gz'.format(
        latest_tag)

    tmp_folder = tempfile.mkdtemp()
    tar_gz_file_path = os.path.join(tmp_folder, '{}.tar.gz'.format(latest_tag))

    r = s.get(latest_tar_gz_url)
    with open(tar_gz_file_path, 'wb') as f:
        f.write(r.content)

    with tarfile.open(tar_gz_file_path) as tar:
        tar.extractall(tmp_folder)

    extract_folder = os.path.join(
        tmp_folder, 'naiveproxy-{}'.format(latest_tag.lstrip('v'))
    )
    if not os.path.exists(extract_folder):
        raise Exception('Not Found Extract Folder.')

    return {
        "tmp_folder": tmp_folder,
        "tar_gz_file": tar_gz_file_path,
        "extract_folder": extract_folder
    }


def get_pgo_path_and_clang_path():
    tmp_folder, extract_folder = itemgetter('tmp_folder', 'extract_folder')(
        download_and_extract_source()
    )

    with open(os.path.join(extract_folder, 'src', 'chrome/build/linux.pgo.txt')) as f:
        pgo_path = f.read().strip()

    clang_scripts_path = os.path.join(
        extract_folder, 'src', 'tools/clang/scripts', 'update.py'
    )
    clang_scripts = import_module_from_path(
        'clang_scripts', clang_scripts_path
    )
    CLANG_VERSION = clang_scripts.PACKAGE_VERSION
    clang_path = 'clang-{}.tar.xz'.format(CLANG_VERSION)

    shutil.rmtree(tmp_folder)

    return {
        "pgo_path": pgo_path,
        "clang_path": clang_path
    }


def pre_build():
    latest_tag = get_naiveproxy_latest_release_tag()
    _pkgver, _pkgrel = latest_tag.lstrip('v').split('-')
    pkgver = '{}_{}'.format(_pkgver, _pkgrel)

    _PGO_PATH, _clang_path = itemgetter('pgo_path', 'clang_path')(
        get_pgo_path_and_clang_path()
    )

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgver'):
            line = '_pkgver={}'.format(_pkgver)
        elif line.startswith('_pkgrel'):
            line = '_pkgrel={}'.format(_pkgrel)
        elif line.startswith('_PGO_PATH'):
            line = '_PGO_PATH=\'{}\''.format(_PGO_PATH)
        elif line.startswith('_clang_path'):
            line = '_clang_path=\'{}\''.format(_clang_path)
        print(line)

    update_pkgver_and_pkgrel(pkgver, updpkgsums=True)


def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
