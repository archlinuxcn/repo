# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.1.12
pkgrel=8
pkgdesc='Open-source implementation of the Apple Filing Protocol'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://netatalk.sourceforge.net'
license=('GPL')
depends=('avahi>=0.6' 'cracklib' 'dbus-glib' 'dbus-python'
  'libevent' 'libgcrypt>=1.2.3' 'libldap' 'pam' 'tdb>=1.4.5')
replaces=('netatalk-git' 'netatalk2')
backup=('etc/afp.conf'
	'etc/extmap.conf')
install=$pkgname.install
source=(http://downloads.sourceforge.net/project/$pkgname/$pkgname/$pkgver/$pkgname-$pkgver.tar.bz2
  gcc10.patch
  python3.patch)
md5sums=('021d2330cb7f7cd2977aec46299dcc1b'
  '9e0c57f07b100bcdf5229224edf25a2b'
  '8a81f88e01bcb4225e39e667b01dc1c6')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  patch -p0 < "$srcdir/gcc10.patch"
  patch -p0 < "$srcdir/python3.patch"
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  autoreconf -fi
  CFLAGS="-Wno-unused-result -O2" \
    ./configure \
    --prefix=/usr --localstatedir=/var/state --sbindir=/usr/bin --sysconfdir=/etc \
    --enable-silent-rules --enable-pgp-uam \
    --with-init-style=systemd --with-cracklib --with-cnid-cdb-backend \
    --without-libevent --without-tdb
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

