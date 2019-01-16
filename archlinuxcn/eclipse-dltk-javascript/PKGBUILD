# Contributer: Shanto <shanto@hotmail.com>
# Contributor: Jonathan Wiersma <archaur at jonw dot org>
# Contributor: Arthur Zamarin <arthurzam@gmail.com>
# Maintainer: David Rosenstrauch <darose@darose.net>

pkgname=eclipse-dltk-javascript
pkgver=5.6
pkgrel=1
_pkgdate=201608300412
pkgdesc="Javascript IDE for Eclipse"
arch=('i686' 'x86_64')
url="http://www.eclipse.org/dltk/"
license=('EPL')
depends=( "eclipse-dltk-core" "eclipse-antlr-runtime>=3.0.0")
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/technology/dltk/downloads/drops/R${pkgver:0:3}/R-$pkgver-$_pkgdate/${pkgname#eclipse-}-R-$pkgver-$_pkgdate.zip")
md5sums=('543178c48e20c4124f92fd7a8950ee7b')

package() {
	cd $srcdir
	install -dm755 $pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/
	find . -type f -exec install -Dm644 {} \
		$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/{} \;
}
