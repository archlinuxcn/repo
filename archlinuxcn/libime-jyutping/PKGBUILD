# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=libime-jyutping
pkgver=1.0.6
pkgrel=1
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5."
arch=('x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL' 'GPL3')
depends=('fcitx5-chinese-addons')
makedepends=('boost' 'extra-cmake-modules' 'ninja' 'python')
source=("https://download.fcitx-im.org/fcitx5/$pkgname/$pkgname-${pkgver}_dict.tar.xz"{,.sig})
sha512sums=('edf20ae0f4d068111cdce04976fcf0d1c030ce43c4bc596f11b7631f8c4699ce52d5123cbeea8c795f48cdb91417686341e051592b465275fdc1436b989de4b5'
            'SKIP')
validpgpkeys=('2CC8A0609AD2A479C65B6D5C8E8B898CBF2412F9') # Weng Xuetian <wengxt@gmail.com>

build() {
  cd $pkgname-$pkgver

  cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  ninja
}

check() {
  cd $pkgname-$pkgver
  ninja test
}

package() {
  cd $pkgname-$pkgver
  DESTDIR="$pkgdir" ninja install
}
