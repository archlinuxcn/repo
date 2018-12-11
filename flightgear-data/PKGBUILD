# Maintainer: Deon Spengler <deon at spengler dot co dot za>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: William Rea <sillywilly@gmail.com>
# Contributor: Hans Janssen <hans@janserv.xs4all.nl>

pkgname=flightgear-data
pkgver=2018.2.2
_pkgver=${pkgver%.*}
pkgrel=1
pkgdesc="Base-Data for the opensource flight-simulator."
arch=(any)
license=('GPL')
url="http://www.flightgear.org/"
options=(!strip)
source=("https://downloads.sourceforge.net/project/flightgear/release-${_pkgver}/FlightGear-${pkgver}-data.tar.bz2")
sha256sums=('c89b94e4cf3cb7eda728daf6cca6dd051f7a47863776c99fd2f3fe0054400ac4')

package() {
  cd "$srcdir"
  mkdir -p "$pkgdir"/usr/share/flightgear
  mv fgdata/ "$pkgdir"/usr/share/flightgear/data
  chown root:root "$pkgdir"/usr/share/flightgear/data
}
