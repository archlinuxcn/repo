# Maintainer: Jameson Pugh <imntreal@gmail.com>

pkgname=breeze-plymouth
pkgver=5.10.1
pkgrel=1
pkgdesc="Breeze theme for plymouth"
arch=(any)
url='https://projects.kde.org/breeze-plymouth'
license=(LGPL)
depends=(plymouth)
makedepends=(extra-cmake-modules)
source=("http://download.kde.org/stable/plasma/${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=('31a56d551c21c0be5c84a595189ed779928a150d40a4d563a890f56f2b78ca3e')

prepare() {
  mkdir -p "${srcdir}/${pkgname}-${pkgver}/build"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake ..
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
}
