# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>
# Contributor: SJ_UnderWater
# Contributor: Dominik Dingel <mail at wodar dot de>
# Contributor: William Udovich <nerdzrule7 at earthlink dot net>
# Contributor: Farhan Yousaf <farhany at xaviya dot com>

pkgname=netatalk
pkgver=4.0.1
pkgrel=1
pkgdesc='Open-source implementation of the Apple Filing Protocol'
url='https://netatalk.io'
license=('GPL-2.0-or-later')

source=(meson.patch
        https://github.com/Netatalk/${pkgname}/releases/download/${pkgname}-${pkgver//./-}/${pkgname}-${pkgver}.tar.xz)
md5sums=('788265d9100fee191b0d4b60a26c92d8'
         '1704dc454eb6332cd80caae3a5ce28e4')

arch=('x86_64' 'i686' 'pentium4' 'armv6h' 'armv7h' 'aarch64')

makedepends=('docbook-xsl'
             'meson'
             'unicode-character-database')

depends=('acl'
         'avahi>=0.6'
         'bash'
         'db5.3'
         'glib2'
         'glibc'
         'libevent'
         'libldap'
         'libgcrypt'
         'libxcrypt'
         'pam'
         'perl'
         'perl-net-dbus')

optdepends=('cracklib: Weak password detection'
            'libcups: Network printer queues support'
            'krb5: Kerberos user authentication support'
            'libwrap: TCP wrapper support'
            'libtirpc: Quota support'
            'mariadb-libs: MySQL CNID backend support'
            'rpcsvc-proto: Quota support'
            'talloc: AFP Spotlight support'
            'tracker3<=3.7.3: AFP Spotlight support')

conflicts=('netatalk-ddp'
           'netatalk2')

backup=('etc/afp.conf'
        'etc/atalkd.conf'
        'etc/extmap.conf'
        'etc/papd.conf'
        'etc/pam.d/netatalk')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -p1 < ../meson.patch
}

build() {
  docbookver=`pacman -Q docbook-xsl | awk '{split($2,a,"-"); print a[1]}'`
  cd "${srcdir}/${pkgname}-${pkgver}"
  arch-meson . build \
    --localstatedir /var/lib \
    -Dwith-appletalk=true \
    -Dwith-bdb-version=5.3 \
    -Dwith-dbus-sysconf-path=/usr/share/dbus-1/system.d \
    -Dwith-debug=true \
    -Dwith-docbook-path=/usr/share/xml/docbook/xsl-stylesheets-${docbookver} \
    -Dwith-dtrace=false \
    -Dwith-init-hooks=false \
    -Dwith-init-style=systemd \
    -Dwith-lockfile-path=/run/netatalk.pid \
    -Dwith-pam-config-path=/etc/pam.d \
    -Dwith-readmes=false \
    -Dwith-spooldir=/var/spool/netatalk
  meson compile -C build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  meson install -C build --destdir "${pkgdir}"
  install -D -m 0644 ./build/config/afp.conf "${pkgdir}/etc/afp.conf"
  install -D -m 0644 ./build/config/dbus-session.conf "${pkgdir}/etc/dbus-session.conf"
  install -D -m 0644 ./build/config/pam/netatalk "${pkgdir}/etc/pam.d/netatalk"
  install -D -m 0644 ./config/atalkd.conf "${pkgdir}/etc/atalkd.conf"
  install -D -m 0644 ./config/extmap.conf "${pkgdir}/etc/extmap.conf"
  install -D -m 0644 ./config/netatalk-dbus.conf "${pkgdir}/usr/share/dbus-1/system.d/netatalk-dbus.conf"
  install -D -m 0644 ./config/papd.conf "${pkgdir}/etc/papd.conf"
  rm -rf "${pkgdir}/usr/share/doc"
}

