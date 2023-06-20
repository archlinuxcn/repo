# Maintainer: Danilo J. S. Bellini <danilo dot bellini at gmail dot com>
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
pkgname=python2-cairo
pkgver=1.19.1
pkgrel=2
pkgdesc="Python bindings for the cairo graphics library"
arch=('x86_64')
url="https://pycairo.readthedocs.io/en/latest/"
license=('LGPL2.1' 'MPL')
depends=(cairo python2)
_github='https://github.com/pygobject/pycairo'
source=("$_github/releases/download/v$pkgver/pycairo-$pkgver.tar.gz")
sha256sums=('2c143183280feb67f5beb4e543fd49990c28e7df427301ede04fc550d3562e84')

prepare() {
  cd "pycairo-$pkgver"
  sed -i 's/raise.*Python 2.*$/pass/' setup.py
}

build() {
  cd "pycairo-$pkgver"
  python2 setup.py build
}

package() {
  cd "pycairo-$pkgver"
  python2 setup.py install --skip-build --root="${pkgdir}" --optimize='1'
}
