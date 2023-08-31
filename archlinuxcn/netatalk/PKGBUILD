# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.1.15
pkgrel=2
pkgdesc='Open-source implementation of the Apple Filing Protocol'
url='https://netatalk.sourceforge.io'
license=('GPL2')

source=(https://github.com/Netatalk/${pkgname}/releases/download/${pkgname}-${pkgver//./-}/${pkgname}-${pkgver}.tar.bz2)
md5sums=('ae542961a541ee786c8ac33daba2e00f')

arch=('i686'
      'x86_64'
      'armv6h'
      'armv7h'
      'aarch64')

depends=('acl'
         'avahi>=0.6'
         'cracklib'
	 'dbus-glib'
	 'dbus-python'
         'libevent'
	 'mariadb-libs'
	 'perl'
	 'python'
	 'tdb>=1.4.5')

conflicts=('netatalk-ddp'
	   'netatalk2')

backup=('etc/afp.conf'
	'etc/extmap.conf')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --sbindir=/usr/bin \
    --sysconfdir=/etc \
    --localstatedir=/var/state \
    --enable-silent-rules \
    --enable-pgp-uam \
    --with-init-style=systemd \
    --with-cracklib \
    --with-cnid-cdb-backend \
    --without-tdb
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

