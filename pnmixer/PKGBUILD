# Maintainer: Brian Bidulock <bidulock@openss7.org>
pkgname=pnmixer
pkgver=0.5.1
pkgrel=3
pkgdesc="GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
groups=('pnmixer')
depends=('gtk2' 'alsa-lib')

source=(https://github.com/downloads/nicklan/pnmixer/pnmixer-${pkgver}.tar.gz pnmixer-0.5.1-configure.in.patch)
md5sums=('2288af95ab280721b39b7c33601d5dd4'
         'd7aef8eb1cec18858fb2faefe6584276')
build() {
  cd $pkgname-$pkgver

  patch -Np0 -i ../pnmixer-0.5.1-configure.in.patch
  ./autogen.sh
  ./configure --prefix=/usr
  make
}
package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
