# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-pyptt
_pkgname=PyPtt
pkgver=0.9.20
pkgrel=1
pkgdesc='A PTT library that support PTT and PTT2'
arch=(any)
url='https://github.com/PttCodingMan/PyPtt'
license=(LGPL3)
depends=(python python-progressbar python-websockets python-uao
         python-beautifulsoup4 python-requests)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/P/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('08ceefd1d05b569b1186f0e3b9b7ce6a2ef576f2199a3a169acbc2f583de9afd')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

# no check() as testing requires a real PTT account

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
