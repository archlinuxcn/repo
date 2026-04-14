# SPDX-FileCopyrightText: Arch Linux contributors
# SPDX-License-Identifier: 0BSD

# Maintainer: gesh <gesh@gesh.uni.cx>
# Contributor: Mark Wagie <mark dot wagie at proton dot me>

pkgname=python-types-docutils
_name=types_docutils
pkgver=0.22.3.20260408
pkgrel=1
pkgdesc="Typing stubs for docutils"
arch=('any')
url="https://github.com/python/typeshed"
license=('Apache-2.0')
depends=('python')
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('22d5d45e4e0d65a1bc8280987a73e28669bb1cc9d16b18d0afc91713d1be26da')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
