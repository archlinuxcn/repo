# Contributer: Shanto <shanto@hotmail.com>
# Contributor: Jonathan Wiersma <archaur at jonw dot org>
# Contributor:: Arthur Zamarin <arthurzam@gmail.com>
# Maintainer: David Rosenstrauch <darose@darose.net>

pkgname=eclipse-dltk-core
pkgver=5.6
pkgrel=1
_pkgdate="201608300412"
pkgdesc="Support for dynamic languages in Eclipse"
arch=('i686' 'x86_64')
url="http://www.eclipse.org/dltk/"
license=('EPL')
depends=("eclipse-emf")
replaces=("eclipse-dltk-core-index")
optdepends=("eclipse-dltk-core-index" "eclipse-dltk-javascript" "eclipse-dltk-mylyn" "eclipse-dltk-python" "eclipse-dltk-rse" "eclipse-dltk-ruby" "eclipse-dltk-tcl")
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/technology/dltk/downloads/drops/R${pkgver:0:3}/R-$pkgver-$_pkgdate/${pkgname#eclipse-}-R-$pkgver-$_pkgdate.zip")
md5sums=('2223370ba7db23248858523659c7adcd')

package() {
	_dest=$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/eclipse
	cd $srcdir
	install -dm755 $_dest
	find features plugins -type f -exec \
		install -Dm644 {} $_dest/{} \;
	# DLTK requires features/*.jar files extracted
	find $_dest/features -type f -name '*.jar' | while read f; do
		install -dm755 ${f%*.jar} && cd ${f%*.jar}
		jar xf $f && rm $f
	done
}
