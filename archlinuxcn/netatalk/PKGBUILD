# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=3.2.7
pkgrel=1
pkgdesc='Open-source implementation of the Apple Filing Protocol'
url='https://netatalk.io'
license=('GPL2')

source=(https://github.com/Netatalk/${pkgname}/releases/download/${pkgname}-${pkgver//./-}/${pkgname}-${pkgver}.tar.xz)
md5sums=('3b1680c4dfd24d0b2236f5612e950911')

arch=('x86_64' 'i686' 'pentium4' 'armv6h' 'armv7h' 'aarch64')

depends=('acl'
         'avahi>=0.6'
         'cracklib'
         'db'
         'dbus-glib'
         'libevent'
         'libgcrypt'
         'pam'
         'perl'
         'perl-net-dbus')

optdepends=('libwrap: TCP wrapper support'
            'mariadb-libs: MySQL CNID backend support'
            'talloc: AFP Spotlight support'
            'tracker3: AFP Spotlight support')

conflicts=('netatalk-ddp'
           'netatalk2')

backup=('etc/afp.conf'
        'etc/extmap.conf'
        'etc/pam.d/netatalk')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./bootstrap
  ./configure \
    --enable-pgp-uam \
    --localstatedir=/var/lib \
    --prefix=/usr \
    --runstatedir=/run \
    --sbindir=/usr/bin \
    --sysconfdir=/etc \
    --with-acls=yes \
    --with-cracklib \
    --with-dbus-sysconf-dir=/usr/share/dbus-1/system.d \
    --with-init-style=systemd \
    --with-lockfile=/run/netatalk.pid \
    --with-pam-confdir=/etc/pam.d \
    --with-tracker-pkgconfig-version=3.0
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

