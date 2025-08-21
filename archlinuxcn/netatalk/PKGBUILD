# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=4.3.0
pkgrel=2
pkgdesc='Open-source implementation of the Apple Filing Protocol'
url='https://netatalk.io'
license=('GPL-2.0-or-later')

source=("https://github.com/Netatalk/${pkgname}/releases/download/${pkgname}-${pkgver//./-}/${pkgname}-${pkgver}.tar.xz")

md5sums=('c7ca0f798102eb97a8e4e26766412a74')

arch=('x86_64' 'i686' 'pentium4' 'armv6h' 'armv7h' 'aarch64')

makedepends=('cmark'
             'meson'
             'unicode-character-database')

depends=('acl'
         'bash'
         'bstring'
         'db5.3'
         'glib2'
         'glibc'
         'iniparser'
         'libevent'
         'libldap'
         'libgcrypt'
         'libxcrypt'
         'pam'
         'perl'
         'perl-net-dbus')

optdepends=('localsearch: AFP Spotlight support'
            'talloc: AFP Spotlight support'
            'tinysparql: AFP Spotlight support'
            'avahi>=0.6: Automatic service discovery support'
            'krb5: Kerberos user authentication support'
            'mariadb-libs: MySQL CNID backend support'
            'libcups: Network printer queues support'
            'libtirpc: Quota support'
            'rpcsvc-proto: Quota support'
            'sqlite3: SQLite CNID backend support'
            'libwrap: TCP wrappers support'
            'cracklib: Weak password detection')

conflicts=('netatalk-ddp'
           'netatalk2')

backup=('etc/afp.conf'
        'etc/atalkd.conf'
        'etc/extmap.conf'
        'etc/papd.conf'
        'etc/pam.d/netatalk')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}" || exit 1
  arch-meson . build \
    --localstatedir /var/lib \
    -Dwith-appletalk=true \
    -Dwith-bdb-version=5.3 \
    -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d \
    -Dwith-docs=man \
    -Dwith-dtrace=false \
    -Dwith-init-hooks=false \
    -Dwith-lockfile-path=/run \
    -Dwith-overwrite=true \
    -Dwith-spooldir=/var/spool/netatalk
  meson compile -C build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}" || exit 1
  meson install -C build --destdir "${pkgdir}"
}

