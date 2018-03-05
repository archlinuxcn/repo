# Maintainer: Doug Newgard <scimmia at archlinux dot org>
# Contributor: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Kosyak <ObKo@mail.ru>

pkgname=qextserialport
pkgver=1.2rc
pkgrel=6
pkgdesc='Cross-platform serial port class libary for Qt'
arch=('i686' 'x86_64')
url='https://github.com/qextserialport/qextserialport'
license=('MIT')
depends=('gcc-libs' 'glibc' 'qt5-base')
source=("$pkgname-$pkgver.tar.gz::https://github.com/qextserialport/qextserialport/archive/$pkgver.tar.gz")
sha256sums=('1f1c068206af95c328b165e9ea31006e43faa6ee224aaec6aa0f72d2afa5f011')

prepare() {
  mkdir -p $pkgname-$pkgver/build
}

build() {
  cd $pkgname-$pkgver/build

  qmake-qt5 ..
  make
}

package() {
  cd $pkgname-$pkgver

  make -C build INSTALL_ROOT="$pkgdir" install
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/qextserialport/"

  # Fix wrong path in prl files
  sed -i '/^QMAKE_PRL_BUILD_DIR/d' "$pkgdir/usr/lib/"*.prl
}
