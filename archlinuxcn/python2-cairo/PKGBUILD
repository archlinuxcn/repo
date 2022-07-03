# Maintainer: Angel Velasquez <angvp@archlinux.org>  
# Maintainer: Jan de Groot <jgc@archlinux.org>

pkgname=python2-cairo
pkgver=1.18.2
pkgrel=4
pkgdesc="Python bindings for the cairo graphics library"
arch=('x86_64')
url="https://pycairo.readthedocs.io/en/latest/"
license=('LGPL2.1' 'MPL')
depends=(cairo python2)
makedepends=(git)
_commit=8643af4c10059827056e769c8c7a997bdc3d5a29  # tags/v1.18.2
source=("git+https://github.com/pygobject/pycairo/#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
  cd pycairo
  git describe --tags | sed 's/^v//;s/-/+/g'
}

build() {
  cd pycairo
  python2 setup.py build
}

package() {
  cd pycairo
  python2 setup.py install --skip-build --root="${pkgdir}" --optimize='1'
}
