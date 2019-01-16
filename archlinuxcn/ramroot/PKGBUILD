# Maintainer: Chris Magyar <c.magyar.ec@gmail.com>
pkgname=ramroot
pkgver=1.1.8
pkgrel=1
pkgdesc="Load root filesystem completely to RAM during boot"
arch=('any')
url="https://github.com/arcmags/$pkgname"
license=('GPL')
depends=('sudo')
conflicts=('liveroot')
install=ramroot.install
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
md5sums=('9412771e7ba0736c37d87f05c28abe24')

package() {
	cd "$pkgname-$pkgver"
    install -D -m644 ./lib/etc/issue \
        "$pkgdir/usr/lib/ramroot/etc/issue"
    install -D -m644 ./lib/hooks/ramroot \
        "$pkgdir/usr/lib/ramroot/hooks/ramroot"
    install -D -m644 ./lib/install/ramroot \
        "$pkgdir/usr/lib/ramroot/install/ramroot"
    install -D -m755 ./ramroot \
        "$pkgdir/usr/bin/ramroot"
    install -D -m644 ./lib/man/ramroot.8 \
        "$pkgdir/usr/share/man/man8/ramroot.8"
}
