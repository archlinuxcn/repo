# Maintainer: Wei-Ning Huang <aitjcize@gmail.com>
pkgname=cppman-git
_pkgname=cppman
pkgver=20160424
pkgrel=1
pkgdesc="C++ 98/11/14 manual pages for Linux/MacOS"
arch=("any")
url="https://github.com/aitjcize/cppman"
license=("GPL")
makedepends=(git)
conflicts=(cppman)
depends=(python3 vim groff python-beautifulsoup4 python-html5lib)
source=("git://github.com/aitjcize/${_pkgname}")
sha256sums=("SKIP")


pkgver() {
  date '+%Y%m%d'
}

build() {
  cd ${_pkgname}
  python3 setup.py build
}

package() {
  cd ${_pkgname}
  python3 setup.py install --root=${pkgdir}/ --optimize=1
}
