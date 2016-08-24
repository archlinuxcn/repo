# Maintainer: Yuexuan Gu <lastavengers@outlook.com>
pkgname=pnmixer-gtk3
pkgver=0.7~rc1
_pkgver=${pkgver/\~/-}
pkgrel=1
pkgdesc="A simple mixer application designed to run in your system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
depends=('gtk3' 'alsa-lib' 'libx11' 'libnotify')
makedepends=('intltool')
conflicts=('pnmixer-git' 'pnmixer-gtk2' 'pnmixer')

source=(https://github.com/nicklan/pnmixer/archive/v${_pkgver}.tar.gz)
sha256sums=('2f090a51c218d221b63aa32126ecf405943a42ef09c0a28021d2af44a5ebd4ef')

build() {
  cd ${pkgname%-gtk3}-$_pkgver

  ./autogen.sh
  ./configure --prefix=/usr
  make
}

package() {
  cd ${pkgname%-gtk3}-$_pkgver

  make DESTDIR="$pkgdir" install
}
