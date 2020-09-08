# Maintainer: Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Andya <hugo981@gmx.com>
# Contributor: Lazaros Koromilas <koromilaz@gmail.com>

pkgname=saxon-he
pkgver=10.2
_pkgver=${pkgver//./-}
pkgrel=1
pkgdesc="XSLT 2.0 / XPath 2.0 and 3.0 / XQuery 1.0 and 3.0 processor for Java - Home Edition"
url="http://saxon.sourceforge.net"
license=('MPL')
arch=('any')
depends=('java-runtime-headless')
provides=('java-saxon')
conflicts=('java-saxon')
source=("https://downloads.sourceforge.net/saxon/SaxonHE${_pkgver}J.zip"
        "saxon-xslt.sh"
        "saxon-xquery.sh")
sha256sums=('1cdb9edc158159e940937035464ad4e188bc342e2eda8a1c72e2d02d170d3aa1'
            '355cf52e3e3b35e4db5dd098fbd57335d20ed10ae070c57a6de214859d04719f'
            'dd42ecae1ef7ff371642148b4ed49fadee0d5b2333c14e138edaae7269ab2199')

package() {
    cd "$srcdir"
    install -Dm644 $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/$pkgname-$pkgver.jar"
    install -Dm755 saxon-xslt.sh "$pkgdir/usr/bin/saxon-xslt"
    install -Dm755 saxon-xquery.sh "$pkgdir/usr/bin/saxon-xquery"
    # link with simpler name for compat with others
    ln -s $pkgname-$pkgver.jar "$pkgdir/usr/share/java/saxon/saxon.jar"
    ln -s saxon-xslt "$pkgdir/usr/bin/saxon"
}
