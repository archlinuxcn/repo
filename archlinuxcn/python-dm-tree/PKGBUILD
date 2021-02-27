# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-dm-tree
pkgver=0.1.5
pkgrel=1
pkgdesc='tree is a library for working with nested data structures'
arch=('any')
url='https://tree.readthedocs.io'
license=('Apache-2.0')
depends=(python python-six)
optdepends=()
makedepends=(python python-setuptools bazel)
source=("$pkgname-$pkgver::https://pypi.org/packages/source/d/dm-tree/dm-tree-${pkgver}.tar.gz")
sha256sums=('a951d2239111dfcc468071bc8ff792c7b1e3192cab5a3c94d33a8b2bda3127fa')

_pkgname=dm-tree

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
}
