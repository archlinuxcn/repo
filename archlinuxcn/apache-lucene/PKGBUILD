# Maintainer: Jingbei Li <i@jingbei.li>
# Co-Maintainer: Felix Golatofski <contact@xdfr.de>

_pkgname=lucene
pkgname=apache-$_pkgname
pkgver=8.6.0
pkgrel=1
pkgdesc="Apache Lucene is a high-performance, full-featured text search engine library written entirely in Java."
arch=('any')
url="https://lucene.apache.org/"
license=('Apache')
depends=('java-runtime')
source=("https://downloads.apache.org/$_pkgname/java/$pkgver/$_pkgname-$pkgver.tgz")
sha256sums=('0f2a17d089da273d16c87c18c6ab02dc13816ed17ffd7cf82b1254888ba42f34')

package() {
	cd "${srcdir}/$_pkgname-$pkgver"
	mkdir -p $pkgdir/usr/share/java/$pkgname
	find . -type f -name '*.jar' -exec mv {} $pkgdir/usr/share/java/$pkgname \;
	install -Dm644 "LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
