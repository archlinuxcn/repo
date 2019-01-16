# Contributor: Jonathan Wiersma <archaur at jonw dot org>
# Maintainer: David Rosenstrauch <darose@darose.net>

pkgname=eclipse-antlr-runtime
pkgver=3.0.0
pkgrel=3
pkgdesc="Support for antlr parser generator in Eclipse"
arch=('i686' 'x86_64')
url="http://antlreclipse.sourceforge.net/"
license=('EPL')
depends=("eclipse")
noextract=($pkgname-$pkgver.jar)
source=("$pkgname-$pkgver.jar::http://www.eclipse.org/downloads/download.php?file=/tools/orbit/downloads/drops/R20090529135407/bundles/org.antlr.runtime_3.0.0.v200803061811.jar")
md5sums=('9cd7fd8e700918f605496a0aad5af4b8')

package() {
    install -d "$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/eclipse/plugins"
    install -m644 "$srcdir/$pkgname-$pkgver.jar" \
    	"$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/eclipse/plugins"
}
