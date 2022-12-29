# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-pyptt
_pkgname=PyPtt
pkgver=1.0.4
pkgrel=1
pkgdesc='A PTT library that support PTT and PTT2'
arch=(any)
url='https://github.com/PttCodingMan/PyPtt'
license=(LGPL3)
depends=(python python-progressbar python-websockets python-uao
         python-beautifulsoup4 python-requests)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/P/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('7c0dd20b2438e7f2a049bd882cb037380f8b0eab44b8e9c7822cf93430a998a0')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

# no check() as testing requires a real PTT account

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
