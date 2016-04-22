# Maintainer: SanskritFritz (gmail)

pkgname=netdata

pkgver=1.1.0
pkgrel=1
pkgdesc="Real-time performance monitoring, in the greatest possible detail, over the web."
url="https://github.com/firehol/netdata/wiki"
arch=('i686' 'x86_64')
license=('GPL')
depends=('libmnl' 'libnetfilter_acct' 'zlib')
optdepends=('nodejs: Webbox plugin')
source=("http://firehol.org/download/netdata/releases/v$pkgver/netdata-$pkgver.tar.xz")
backup=('etc/netdata/netdata.conf' 'etc/netdata/charts.d.conf' 'etc/netdata/apps_groups.conf')
install="$pkgname.install"

build() {
	cd "$pkgname-$pkgver"

	./autogen.sh
	./configure \
		--prefix="/usr" \
		--sbindir="/usr/bin" \
		--sysconfdir="/etc" \
		--libexecdir="/usr/lib" \
		--localstatedir="/var" \
		--with-zlib --with-math --with-user=netdata \
		CFLAGS="-O3"
	make
}

package() {
	cd "$pkgname-$pkgver"

	make DESTDIR="$pkgdir" install

	touch "$pkgdir/etc/netdata/netdata.conf"

	install -Dm0644 "system/netdata.service" "$pkgdir/usr/lib/systemd/system/netdata.service"
}

md5sums=('19e6d2b142906f824d0951428d0c030e')
