# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-pyptt
_pkgname=PyPtt
pkgver=0.9.24
pkgrel=1
pkgdesc='A PTT library that support PTT and PTT2'
arch=(any)
url='https://github.com/PttCodingMan/PyPtt'
license=(LGPL3)
depends=(python python-progressbar python-websockets python-uao
         python-beautifulsoup4 python-requests)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/P/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('f222cefc097e95829501d2499a6ad813f6e7abab3fc4a24de17f97674dc39226')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

# no check() as testing requires a real PTT account

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
