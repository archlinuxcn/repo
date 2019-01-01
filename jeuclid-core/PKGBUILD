# Maintainer: Alucryd <alucryd at gmail dot com>
# Maintainer: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=jeuclid-core
pkgver=3.1.9
pkgrel=1
pkgdesc="MathML renderer for Java"
arch=('any')
url="http://jeuclid.sourceforge.net/"
license=(APACHE)
depends=('java-runtime')
source=("http://downloads.sourceforge.net/jeuclid/jeuclid-minimal-$pkgver-distribution.zip")
md5sums=('c89067cdb005008f2ad46d579ed2086b')

package() {
    install -Dm644 $srcdir/jeuclid-minimal-$pkgver/repo/$pkgname-$pkgver.jar $pkgdir/usr/share/java/jeuclid/$pkgname.jar
}
