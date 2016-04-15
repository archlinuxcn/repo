# Maintainer: SanskritFritz (gmail)

pkgname=netdata

pkgver=1.0.0
pkgrel=2
pkgdesc="Real-time performance monitoring, in the greatest possible detail, over the web."
url="https://github.com/firehol/netdata/wiki"
arch=('i686' 'x86_64')
license=('GPL')
depends=('libmnl' 'libnetfilter_acct' 'zlib')
optdepends=('nodejs: Webbox plugin')
source=("http://firehol.org/download/netdata/releases/v$pkgver/netdata-$pkgver.tar.xz")
backup=('etc/netdata/netdata.conf' 'etc/netdata/charts.d.conf' 'etc/netdata/apps_groups.conf')
install="$pkgname.install"

prepare() {
	cd "$pkgname-$pkgver"
	sed -i "s#/usr/sbin/netdata#/usr/bin/netdata#" "system/netdata-systemd"
	sed -i "s#/bin/kill#/usr/bin/kill#" "system/netdata-systemd"
	# http://article.gmane.org/gmane.comp.security.firewalls.firehol.devel/898
	# sed -i "s#<script>var netdataTheme = 'slate';</script>##" "web/index.html"
}

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
	install -Dm0644 "system/netdata-systemd" "$pkgdir/usr/lib/systemd/system/netdata.service"
}

md5sums=('2bc87c905c2e511e9077c92e0d1cba3e')
