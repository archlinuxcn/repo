# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Rustam Tsurik <rustam.tsurik@gmail.com>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>

pkgname=('mysql' 'libmysqlclient' 'mysql-clients')
pkgbase=mysql
pkgver=8.0.15
pkgrel=1
pkgdesc="Fast SQL database server, community edition"
arch=('x86_64')
makedepends=('openssl' 'zlib' 'cmake' 'systemd-tools' 'libaio' 'jemalloc'
             'rpcsvc-proto' 'libtirpc' 'icu' 'libedit' 'libevent' 're2'
             'rapidjson' 'protobuf')
license=('GPL')
url="https://www.mysql.com/products/community/"
options=('!libtool' '!ccache') # Sorry but actually ccache is not supported
source=("https://cdn.mysql.com/Downloads/MySQL-8.0/${pkgbase}-boost-${pkgver}.tar.gz"
        "mysqld-post.sh"
        "mysqld-tmpfile.conf"
        "mysqld.service"
        "my-default.cnf"
        "mysql-ld.so.conf")
sha256sums=('95dbdb54c3967feefb255b96458b089a601e4de238bcc1f328b066018ee47db0'
            '368f9fd2454d80eb32abb8f29f703d1cf9553353fb9e1ae4529c4b851cb8c5dd'
            '2af318c52ae0fe5428e8a9245d1b0fc3bc5ce153842d1563329ceb1edfa83ddd'
            '50212165bdb09855b97b15a917464ba34f82edf30a0c43f9a0c93a27071df556'
            '3cc3ba4149fb2f9e823601b9a414ff5b28a2a52f20bc68c74cc0505cf2d1832d'
            'e1c23fa0971a13d998f2790379b68c475438d05b6d6f2691b99051dbf497567f')

build() {
  rm -rf build
  mkdir build
  cd build

  cmake "../${pkgbase}-${pkgver}" \
    -DCMAKE_AR=/usr/bin/gcc-ar \
    -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
    -DBUILD_CONFIG=mysql_release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DSYSCONFDIR=/etc/mysql \
    -DMYSQL_DATADIR=/var/lib/mysql \
    -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock \
    -DENABLED_LOCAL_INFILE=ON \
    -DINSTALL_INFODIR=share/mysql/docs \
    -DINSTALL_MANDIR=share/man \
    -DINSTALL_PLUGINDIR=lib/mysql/plugin \
    -DINSTALL_SCRIPTDIR=bin \
    -DINSTALL_INCLUDEDIR=include/mysql \
    -DINSTALL_DOCREADMEDIR=share/mysql \
    -DINSTALL_SUPPORTFILESDIR=share/mysql \
    -DINSTALL_MYSQLSHAREDIR=share/mysql \
    -DINSTALL_DOCDIR=share/mysql/docs \
    -DINSTALL_SHAREDIR=share/mysql \
    -DWITH_SYSTEM_LIBS=ON \
    -DWITH_LIBWRAP=OFF \
    -DCMAKE_EXE_LINKER_FLAGS='-ljemalloc' \
    -DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
    -DWITHOUT_FEDERATED_STORAGE_ENGINE=ON \
    -DCMAKE_C_FLAGS="${CFLAGS}" \
    -DCMAKE_C_LINK_FLAGS="${LDFLAGS}" \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS}" \
    -DCMAKE_CXX_LINK_FLAGS="${LDFLAGS}" \
    -DWITH_BOOST="../${pkgname}-${pkgver}/boost"
  make
}

package_libmysqlclient(){
  pkgdesc="MySQL client libraries"
  depends=('libsasl' 'zlib')
  conflicts=('libmariadbclient' 'mariadb-libs')
  provides=("libmariadbclient=${pkgver}" "libmysqlclient=${pkgver}" "mariadb-libs=${pkgver}")

  cd build
  for dir in include libmysql libservices
  do
    make -C "${dir}" DESTDIR="${pkgdir}" install
  done

  install -m 755 -d "${pkgdir}/usr/bin"
  install -m 755 scripts/mysql_config "${pkgdir}/usr/bin/"
  install -m 755 -d "${pkgdir}/usr/share/man/man1"
  for man in mysql_config
  do
    install -m 644 "${srcdir}/${pkgbase}-${pkgver}/man/${man}.1" "${pkgdir}/usr/share/man/man1/${man}.1"
  done
}

package_mysql-clients(){
  pkgdesc="MySQL client tools"
  depends=('libmysqlclient' 'zlib' 'openssl' 'jemalloc' 'libedit' 'lz4')
  conflicts=('mariadb-clients')
  provides=("mariadb-clients=${pkgver}" "mysql-clients=${pkgver}")

  cd build
  make -C "client" DESTDIR="${pkgdir}" install

  # install man pages
  install -d "${pkgdir}/usr/share/man/man1"
  for man in mysql mysqladmin mysqlcheck mysqldump mysqlimport mysqlshow mysqlslap
  do
    install -m644 "${srcdir}/${pkgbase}-${pkgver}/man/${man}.1" "${pkgdir}/usr/share/man/man1/${man}.1"
  done

  # provided by mysql
  rm "${pkgdir}/usr/bin/mysql_upgrade"
  rm "${pkgdir}/usr/bin/mysql_config_editor"
  rm "${pkgdir}/usr/bin/mysqlbinlog"
  rm "${pkgdir}/usr/bin/mysql_secure_installation"
  rm "${pkgdir}/usr/bin/mysql_ssl_rsa_setup"
  rm "${pkgdir}/usr/bin/mysqltest"
}

package_mysql(){
  pkgdesc="Fast SQL database server, community edition"
  backup=('etc/mysql/my.cnf')
  install="${pkgbase}.install"
  depends=('mysql-clients' 'libsasl' 'zlib' 'jemalloc' 'libaio' 'libtirpc' 'icu'
           'lz4' 'libevent' 'protobuf')
  conflicts=('mariadb')
  provides=("mariadb=${pkgver}" "mysql=${pkgver}")
  options=('emptydirs')

  cd build
  make DESTDIR="${pkgdir}" install

  install -m 644 -D "${srcdir}/my-default.cnf" "${pkgdir}/etc/mysql/my.cnf"
  install -m 755 -D "${srcdir}/mysqld-post.sh" "${pkgdir}/usr/bin/mysqld-post"
  install -m 644 -D "${srcdir}/mysqld-tmpfile.conf" "${pkgdir}/usr/lib/tmpfiles.d/mysqld.conf"
  install -m 755 -d "${pkgdir}/usr/lib/systemd/system"
  install -m 644 -D "${srcdir}/mysqld.service" "${pkgdir}/usr/lib/systemd/system/"
  install -m 755 -d "${pkgdir}/etc/ld.so.conf.d"
  install -m 644 -D "${srcdir}/mysql-ld.so.conf" "${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf"

  # provided by libmysqlclient
  rm "${pkgdir}/usr/bin/mysql_config"
  rm "${pkgdir}/usr/lib/libmysqlclient.so"
  rm "${pkgdir}/usr/lib/libmysqlclient.so.21"
  rm "${pkgdir}/usr/lib/libmysqlclient.so.21.0.15"
  rm "${pkgdir}/usr/lib/libmysqlservices.a"
  rm "${pkgdir}/usr/lib/mysql/plugin/authentication_ldap_sasl_client.so"
  rm -r "${pkgdir}/usr/include/"
  rm "${pkgdir}/usr/share/man/man1/mysql_config.1"

  # provided by mysql-clients
  rm "${pkgdir}/usr/bin/mysql"
  rm "${pkgdir}/usr/bin/mysqladmin"
  rm "${pkgdir}/usr/bin/mysqlcheck"
  rm "${pkgdir}/usr/bin/mysqldump"
  rm "${pkgdir}/usr/bin/mysqlimport"
  rm "${pkgdir}/usr/bin/mysqlpump"
  rm "${pkgdir}/usr/bin/mysqlshow"
  rm "${pkgdir}/usr/bin/mysqlslap"
  rm "${pkgdir}/usr/share/man/man1/mysql.1"
  rm "${pkgdir}/usr/share/man/man1/mysqladmin.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlcheck.1"
  rm "${pkgdir}/usr/share/man/man1/mysqldump.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlimport.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlshow.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlslap.1"

  # not needed
  rm -r "${pkgdir}/usr/mysql-test"
  rmdir "${pkgdir}/usr/run"

  # Move somewhere else
  mv "${pkgdir}/usr/LICENSE.router" "${pkgdir}/usr/share/mysql/docs"
  mv "${pkgdir}/usr/README.router" "${pkgdir}/usr/share/mysql/docs"

  # Fix permissions
  chmod 755 "${pkgdir}/usr"
}

