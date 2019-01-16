# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.1.12
pkgrel=1
pkgdesc='Open-source implementation of the Apple Filing Protocol'
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url='http://netatalk.sourceforge.net'
license=('GPL')
depends=('avahi>=0.6' 'libldap' 'libgcrypt>=1.2.3' 'libevent' 'python2' 'dbus-glib' 'python2-dbus' 'pam')
replaces=('netatalk-git' 'netatalk2')
backup=('etc/afp.conf'
	'etc/extmap.conf')
install=$pkgname.install
source=(http://downloads.sourceforge.net/project/$pkgname/$pkgname/$pkgver/$pkgname-$pkgver.tar.bz2
	python2.patch)
md5sums=('021d2330cb7f7cd2977aec46299dcc1b'
	'97bc0467dd8a866d9f0835d6440e3c19')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	patch -p0 < "$srcdir/python2.patch"
}

build() {
	cd "$srcdir/$pkgname-$pkgver"
	autoreconf -fi
	CFLAGS="-Wno-unused-result -O2" \
		./configure --prefix=/usr --localstatedir=/var/state --sysconfdir=/etc \
		--sbindir=/usr/bin --enable-silent-rules --with-init-style=systemd \
		--with-cracklib --with-cnid-cdb-backend --enable-pgp-uam --with-libevent=no
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
}
