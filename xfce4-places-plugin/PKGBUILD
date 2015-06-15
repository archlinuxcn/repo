# Maintainer: Alessio Sergi <asergi at archlinux dot us>
pkgname=xfce4-places-plugin
pkgver=1.7.0
pkgrel=2
pkgdesc="Places menu plugin for the Xfce panel"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin"
license=('GPL2')
depends=('libnotify' 'xfce4-panel')
makedepends=('intltool')
source=("http://archive.xfce.org/src/panel-plugins/$pkgname/${pkgver%.*}/$pkgname-${pkgver}.tar.bz2")
sha256sums=('4175c614749abbb5bcf6f49c88125fb0dd36db69f4c374df23563907b16e2c3f')

build() {
  cd "$pkgname-$pkgver"
  # add compatibility for inline functions
  CFLAGS=-fgnu89-inline ./configure \
	      --prefix=/usr \
              --sysconfdir=/etc \
              --libexecdir=/usr/lib \
              --localstatedir=/var \
              --disable-static \
              --disable-debug
  make
}
package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
