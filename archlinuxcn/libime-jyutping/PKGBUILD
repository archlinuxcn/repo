# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=libime-jyutping
pkgver=1.0.14
pkgrel=1
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5."
arch=('x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL-2.1-or-later')
depends=('fcitx5-chinese-addons')
makedepends=('boost' 'extra-cmake-modules' 'fmt' 'ninja')
# source tarball format changed to .tar.zst since 1.10.11
source=("https://download.fcitx-im.org/fcitx5/$pkgname/$pkgname-${pkgver}_dict.tar.zst"{,.sig})
sha512sums=('9a8778c43c3b28ba18c5b6c0b62e79ef61d31815c24ace244e2ba211b435e0a3b29976fb891dce46019a8f94140479809d7d69829e401b371510e4dc961c437f'
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
