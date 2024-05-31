# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=libime-jyutping
pkgver=1.0.12
pkgrel=1
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5."
arch=('x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL-2.1-or-later')
depends=('fcitx5-chinese-addons')
makedepends=('boost' 'extra-cmake-modules' 'fmt' 'ninja')
# source tarball format changed to .tar.zst since 1.10.11
source=("https://download.fcitx-im.org/fcitx5/$pkgname/$pkgname-${pkgver}_dict.tar.zst"{,.sig})
sha512sums=('1417d2611fd3abb7c997b00399ee341cd863ef0a7f8a93b6fc713888762629d4e59e92e92be2400067327e4f646cab5525053f93c27de87974c7c4faced21258'
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
