# Maintainer: Miguel Revilla <yo@miguelrevilla.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=proftpd
pkgver=1.3.7a
pkgrel=2
epoch=2
pkgdesc='High-performance, scalable FTP server'
arch=('x86_64' 'i686')
url='http://www.proftpd.org/'
license=('GPL')
depends=('mariadb-libs' 'postgresql-libs' 'libcap' 'pam' 'hiredis')
backup=('etc/proftpd.conf')
options=('!emptydirs')
source=("ftp://ftp.proftpd.org/distrib/source/${pkgname}-${pkgver}.tar.gz"
        'proftpd.logrotate' 'proftpd.service'
        'proftpd.tmpfiles')
md5sums=('4a9b8877b2e9b08d70e71ad56c19e2c9'
         '4d7a3eedc1852d4fa9faafc072fb8320'
         'f7e0c3a402a845ba8d546b2801f77ed2'
         '907b149a120b046f05647c73502e23c9')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  ./configure --prefix=/usr \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib \
    --disable-pam \
    --with-modules=mod_digest:mod_sftp:mod_quotatab:mod_quotatab_sql:mod_quotatab_file:mod_tls:mod_tls_shmcache:mod_ldap:mod_sql:mod_sql_mysql:mod_sql_postgres:mod_facl:mod_dynmasq \
    --sysconfdir=/etc \
    --localstatedir=/run/proftpd \
    --enable-ctrls \
    --enable-ipv6 \
    --with-includes=/usr/include/mysql:/usr/include/postgresql \
    --with-libraries=/usr/lib/mysql:/usr/lib/postgresql \
    --enable-nls \
    --enable-redis \
    --enable-facl \
    --with-systemd

  make CFLAGS="$CFLAGS -fcommon"
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
  sed -i 's|nogroup|nobody|g' "${pkgdir}/etc/proftpd.conf"

  install -Dm644 ../proftpd.logrotate "${pkgdir}/etc/logrotate.d/proftpd"
  install -Dm755 contrib/xferstats.holger-preiss "${pkgdir}/usr/bin/ftpstats"

  install -d "${pkgdir}/usr/lib/systemd/system/"
  install -m644 "${srcdir}"/proftpd.service "${pkgdir}/usr/lib/systemd/system/"
  install -Dm644 "${srcdir}"/proftpd.tmpfiles \
    "${pkgdir}"/usr/lib/tmpfiles.d/proftpd.conf

  # /run is tmpfs
  rmdir "${pkgdir}"/run/{proftpd,}
}

# vim:set ts=2 sw=2 et:
