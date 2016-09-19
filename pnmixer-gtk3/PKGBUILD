# Maintainer: Yuexuan Gu <lastavengers@outlook.com>
pkgname=pnmixer-gtk3
pkgver=0.7
pkgrel=1
pkgdesc="A simple mixer application designed to run in your system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
depends=('gtk3' 'alsa-lib' 'libx11' 'libnotify')
makedepends=('intltool')
conflicts=('pnmixer-git' 'pnmixer-gtk2' 'pnmixer')

source=(https://github.com/nicklan/pnmixer/archive/v${pkgver}.tar.gz)
sha256sums=('398caf24abd04012c397aa3925a511a6468ec06408c35e38c20ed6789e2798ca')

build() {
  cd ${pkgname%-gtk3}-$pkgver

  ./autogen.sh
  ./configure --prefix=/usr
  make
}

package() {
  cd ${pkgname%-gtk3}-$pkgver

  make DESTDIR="$pkgdir" install
}
