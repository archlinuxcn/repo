# $Id: PKGBUILD 230840 2015-02-05 20:20:07Z dan $
# Maintainer: Dan McGee <dan@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbase=postgresql
pkgbase=binx32-postgresql
pkgname=('libx32-postgresql-libs' 'binx32-postgresql')
pkgver=9.4.1
_majorver=${pkgver%.*}
pkgrel=1.1
arch=('x86_64')
url="http://www.postgresql.org/"
license=('custom:PostgreSQL')
makedepends=('libx32-krb5' 'libx32-libxml2' 'libx32-openssl>=1.0.0' 'libx32-pam')
#makedepends=('libx32-krb5' 'libx32-libxml2' 'binx32-python2' 'binx32-perl' 'binx32-tcl>=8.6.0' 'libx32-openssl>=1.0.0' 'libx32-pam')
source=(http://ftp.postgresql.org/pub/source/v${pkgver}/postgresql-${pkgver}.tar.bz2
        x32.patch
        postgresql-run-socket.patch
        postgresql.pam postgresql.logrotate
        postgresql.service postgresql.tmpfiles.conf postgresql-check-db-dir)
md5sums=('2cf30f50099ff1109d0aa517408f8eff'
         'e7fcec0b799f776e06c7400fab13302a'
         '170486b408ad3b6b24ae91b9196cb004'
         '96f82c38f3f540b53f3e5144900acf17'
         '951d1306d84450d603c47318833bb99d'
         '22809c2ab5f733b51abcef82f315b31c'
         '4ad974e4659d4474a40c54995ed5a809'
         'eb6a2a084db77e9bb9ebb203b712fae5')
sha256sums=('29ddb77c820095b8f52e5455e9c6c6c20cf979b0834ed1986a8857b84888c3a6'
            '15e068dd4896f56eaafd405945c5b57d0b9812e790328d8fc96dc1cbcb3cb10e'
            'f8c444140755e99b1ffd808404bda77c360c2843d13f6270b8dbd067d129b33a'
            '57dfd072fd7ef0018c6b0a798367aac1abb5979060ff3f9df22d1048bb71c0d5'
            'cc766679b3f1dd1e1fe1d4428b747ab44b8778c4127dc011cafd491842756e41'
            '89b061802eee198218c2936ca02ac61be90c46a3e76ebbe2ffa2f60c1cf07cba'
            '27f3ef84f59a008ee9a2324730386e11f68a9b10bbcd7ee4bbdbf4693b08d00d'
            'aa3802f39e2ba5cbaf373c7217894e2212e72a33f4247fe2cc5c1bfc6aad1986')

build() {
  cd "${srcdir}/postgresql-${pkgver}"

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  patch -Np1 < ../postgresql-run-socket.patch
  patch -Np1 < ../x32.patch

  ./configure \
    --prefix=/usr \
    --libdir=/usr/libx32 \
    --mandir=/usr/share/man \
    --datadir=/usr/share/postgresql \
    --sysconfdir=/etc \
    --with-gssapi \
    --with-libxml \
    --with-openssl \
    --without-perl \
    --without-python \
    --without-tcl \
    --with-pam \
    --with-system-tzdata=/usr/share/zoneinfo \
    --enable-nls \
    --enable-thread-safety

  make world
}

package_libx32-postgresql-libs() {
  pkgdesc="Libraries for use with PostgreSQL (x32 ABI)"
  depends=('libx32-krb5' 'libx32-openssl>=1.0.0' 'libx32-readline>=6.0')
  provides=('binx32-postgresql-client')
  conflicts=('binx32-postgresql-client')

  cd "${srcdir}/postgresql-${pkgver}"

  # install libs and non-server binaries
  for dir in src/interfaces src/bin/pg_config src/bin/pg_dump src/bin/psql src/bin/scripts; do
    make -C ${dir} DESTDIR="${pkgdir}" install
  done

  for _x in ${pkgdir}/usr/bin/*; do mv $_x $_x-x32; done
  rm -rf "${pkgdir}"/usr/{share,include}

  cd src/include

  mkdir -p "${pkgdir}"/usr/include

  # these headers are needed by the public headers of the interfaces
  install -m644 pg_config.h "${pkgdir}/usr/include/pg_config-x32.h"
  # TODO: below?
  install -m644 pg_config_manual.h "${pkgdir}/usr/include/pg_config_manual-x32.h"

  # install license
  install -dm755 "$pkgdir"/usr/share/licenses
  ln -s postgresql-libs "${pkgdir}"/usr/share/licenses/libx32-postgresql-libs
}

package_binx32-postgresql() {
  pkgdesc="A sophisticated object-relational DBMS (x32 ABI)"
  backup=('etc/pam.d/postgresql-x32' 'etc/logrotate.d/postgresql-x32')
  depends=("libx32-postgresql-libs>=${pkgver}" 'libx32-krb5' 'libx32-libxml2' 'libx32-readline>=6.0' 'libx32-openssl>=1.0.0' 'libx32-pam' "${_pkgbase}>=9.3")
  optdepends=('postgresql-old-upgrade: upgrade from previous major version using pg_upgrade')
  options=('staticlibs')
  install=postgresql.install

  cd "${srcdir}/postgresql-${pkgver}"

  # install
  make DESTDIR="${pkgdir}" install
  make -C contrib DESTDIR="${pkgdir}" install
  make -C doc/src/sgml DESTDIR="${pkgdir}" install-man

  # we don't want these, they are in the -libs package
  for dir in src/interfaces src/bin/pg_config src/bin/pg_dump src/bin/psql src/bin/scripts; do
    make -C ${dir} DESTDIR="${pkgdir}" uninstall
  done

  rm -rf "${pkgdir}/usr/share"

  # install license
  install -dm755 "${pkgdir}/usr/share/licenses/"
  ln -s ${_pkgbase} "${pkgdir}/usr/share/licenses/binx32-postgresql"

  # clean up unneeded installed items
  rm -rf "${pkgdir}/usr/include/postgresql-x32/internal"
  rm -rf "${pkgdir}/usr/include/libpq"
  find "${pkgdir}/usr/include" -maxdepth 1 -type f -execdir rm {} +

  install -D -m644 "${srcdir}/postgresql.tmpfiles.conf" \
    "${pkgdir}/usr/lib/tmpfiles.d/postgresql-x32.conf"
  install -D -m644 "${srcdir}/postgresql.service" \
    "${pkgdir}/usr/lib/systemd/system/postgresql-x32.service"
  install -D -m755 "${srcdir}/postgresql-check-db-dir" \
    "${pkgdir}/usr/bin/postgresql-check-db-dir"

  install -D -m644 "${srcdir}/postgresql.pam" \
    "${pkgdir}/etc/pam.d/postgresql-x32"

  for _x in ${pkgdir}/usr/bin/*; do mv $_x $_x-x32; done

  install -D -m644 "${srcdir}/postgresql.logrotate" \
    "${pkgdir}/etc/logrotate.d/postgresql-x32"
}
