# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=libime-jyutping
pkgver=1.0.5
pkgrel=2
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5."
arch=('x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL' 'GPL3')
depends=('fcitx5-chinese-addons')
makedepends=('boost' 'extra-cmake-modules' 'ninja' 'python')
source=("https://download.fcitx-im.org/fcitx5/$pkgname/$pkgname-${pkgver}_dict.tar.xz"{,.sig})
sha512sums=('4c2583a23a406276e8d462fc53fd1dd1660ecc7fa0f7bb673e9c8a4c3ab1aec14f172d82bfe74d43b2a7982c96006db61c8347f72fd10ef9af1e08961fd03e0e'
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
