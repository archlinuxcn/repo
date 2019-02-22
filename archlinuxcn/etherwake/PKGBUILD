# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Contributor: Markus Volkmann <mcfock@counterstrike.de>

pkgname=etherwake
pkgver=1.09
pkgrel=7
arch=(i686 x86_64)
pkgdesc="Utility for waking up computers via wake-on-lan (wol)"
license=("GPL")
url="http://www.scyld.com/wakeonlan.html"
depends=("glibc")
source=(https://launchpad.net/ubuntu/+archive/primary/+files/etherwake_1.09.orig.tar.gz)

build() {
	cd "$srcdir/$pkgname-$pkgver.orig"
	rm -f etherwake
	gcc ether-wake.c -o etherwake
}

package() {
	cd "$srcdir/$pkgname-$pkgver.orig"
	install -Dm0755 etherwake "$pkgdir/usr/bin/etherwake"
	install -Dm0644 etherwake.8 "$pkgdir/usr/share/man/man8/etherwake.8"
}

sha256sums=('54241c7689579dc86e29e6afbc6d60e69f97135091a1395c8a10f6d5a2daec1d')
