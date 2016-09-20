# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=pnmixer
pkgver=0.7
pkgrel=1
pkgdesc="GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
makedepends=('intltool')
depends=('gtk2' 'alsa-lib' 'libnotify')
source=("https://github.com/nicklan/pnmixer/releases/download/v0.7/pnmixer-${pkgver}.tar.gz")
md5sums=('4ddfab98ad915075aecced01e0890c65')
build() {
  cd $pkgname-$pkgver
  ./autogen.sh --without-gtk3 --prefix=/usr
  make V=0
}
package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
