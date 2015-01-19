pkgname=sniproxy
pkgver=0.3.6
pkgrel=1
pkgdesc="TLS SNI proxy"
arch=(i686 x86_64)
url="https://github.com/dlundquist/sniproxy"
license=('BSD')
depends=(libev pcre udns)
backup=('etc/sniproxy.conf')
install=sniproxy.install
source=($pkgname-$pkgver.tar.gz::https://github.com/dlundquist/sniproxy/archive/$pkgver.tar.gz
	sniproxy.service
	sniproxy.conf
	sniproxy.tmpfiles.d)
md5sums=('52a01eb55ac7712de2dd13f1ba6260e4'
         '4aa83e863200de912b3415daa1adeca0'
         '86deda1006d9b0ac4bb9f057b517f59b'
         '985de392ad947f91a5e3ec4d5e53c087')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	./autogen.sh
	./configure --prefix=/usr --sbindir=/usr/bin
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
	install -Dm0644 $srcdir/sniproxy.conf $pkgdir/etc/sniproxy.conf
	install -Dm0644 $srcdir/sniproxy.tmpfiles.d $pkgdir/usr/lib/tmpfiles.d/sniproxy.conf
	install -Dm0644 sniproxy.conf $pkgdir/usr/share/doc/$pkgname/sniproxy.conf
	install -Dm0644 COPYING $pkgdir/usr/share/licenses/$pkgname/COPYING
	install -Dm0644 $srcdir/sniproxy.service $pkgdir/usr/lib/systemd/system/sniproxy.service
}
