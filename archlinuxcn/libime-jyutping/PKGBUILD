# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=libime-jyutping
pkgver=1.0.8
pkgrel=1
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5."
arch=('x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL' 'GPL3')
depends=('fcitx5-chinese-addons')
makedepends=('boost' 'extra-cmake-modules' 'fmt' 'ninja')
source=("https://download.fcitx-im.org/fcitx5/$pkgname/$pkgname-${pkgver}_dict.tar.xz"{,.sig})
sha512sums=('68e014c7e48af4dfc98e45424366c1916a63fe082864878a92850d87d7923562c3cdc2e57878316b51603a10fca9f4449caf5911f899e06201e7457f8e365e3a'
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
