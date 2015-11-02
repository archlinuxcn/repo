# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=pnmixer
pkgver=0.6.1
pkgrel=2
pkgdesc="GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
makedepends=('intltool')
depends=('gtk2' 'alsa-lib' 'libnotify')
install="${pkgname}.install"
source=("https://github.com/nicklan/pnmixer/releases/download/v0.6/pnmixer-${pkgver}.tar.gz")
md5sums=('42e026df389901cc1e0a72db0d256fd0')
build() {
  cd $pkgname-$pkgver
  ./autogen.sh --without-gtk3 --prefix=/usr
  make V=0
}
package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
