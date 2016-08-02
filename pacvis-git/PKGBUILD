# Maintainer: Jiachen Yang <farseerfc@gmail.com>

pkgname=pacvis-git
_pkgname=pacvis
pkgver=0.2.0.r8.ge4f2c64
pkgrel=1
pkgdesc="Visualize pacman local database using Vis.js, inspired by pacgraph"
arch=('any')
url="https://github.com/farseerfc/pacvis"
license=('MIT')
depends=('python-tornado' 'pyalpm' 'python-setuptools')
makedepends=('git')
source=("git+https://github.com/farseerfc/pacvis.git")
conflicts=("pacvis")
sha512sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

build () {
    cd "$srcdir/$_pkgname"
    python3 setup.py build
}

package () {
    cd "$srcdir/$_pkgname"
    python3 setup.py install --root="$pkgdir" -O1
}

# vim:set ts=2 sw=2 et:
