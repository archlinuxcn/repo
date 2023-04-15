# Maintainer: Muflone http://www.muflone.com/contacts/english/
# Contributor: Francois Menning <f.menning@pm.me>
# Contributor: Rustam Tsurik <rustam.tsurik@gmail.com>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>

pkgname=('mysql' 'libmysqlclient' 'mysql-clients')
pkgbase=mysql
pkgver=8.0.32
pkgrel=1
pkgdesc="Fast SQL database server, community edition"
arch=('x86_64')
makedepends=('openssl' 'zlib' 'cmake' 'systemd-tools' 'systemd-libs' 'libaio'
             'jemalloc' 'rpcsvc-proto' 'libtirpc' 'icu' 'libedit' 'libevent'
             'libfido2' 're2' 'rapidjson')
license=('GPL')
url="https://www.mysql.com/products/community/"
source=("https://cdn.mysql.com/Downloads/MySQL-8.0/${pkgbase}-boost-${pkgver}.tar.gz"
        "my-default.cnf"
        "mysql-ld.so.conf"
        "mysql.sysconfig"
        "mysqld_service.patch"
        "systemd-tmpfiles.patch"
        "systemd-sysusers.conf")
sha256sums=('1a83a2e1712a2d20b80369c45cecbfcc7be9178d4fc0e81ffba5c273ce947389'
            '6bc24ae510f6b6bbad6b3edda2d0028b29292937b482274a4c2fae335f4de328'
            'e1c23fa0971a13d998f2790379b68c475438d05b6d6f2691b99051dbf497567f'
            '203dcd22fea668477ac7123dbd9909fae72d3d07f8855417a669a9c94db072ae'
            '8fbedfc2c5fe271ed13217feeceeac00202d2cb135e4283eeee2f9a13d6251af'
            '270074dc0a01e0f959590ad95e5bbaaac3f821bb44eba32d039a6aee506b9c6a'
            '200a992eb41c95efa99845d017439ddd4018a3e51f57ffca8cb802b0d25123f1')

build() {
  rm -rf build
  mkdir build
  cd build

  cmake "../${pkgbase}-${pkgver}" \
    -DCMAKE_AR=/usr/bin/gcc-ar \
    -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
    -DBUILD_CONFIG=mysql_release \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
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
    -DROUTER_INSTALL_CONFIGDIR=../etc/mysqlrouter \
    -DROUTER_INSTALL_DATADIR=/var/lib/mysqlrouter \
    -DROUTER_INSTALL_RUNTIMEDIR=/run \
    -DROUTER_INSTALL_LOGDIR=/var/log/mysqlrouter \
    -DWITH_SYSTEM_LIBS=ON \
    -DWITH_FIDO=system \
    -DWITH_SSL=system \
    -DWITH_LIBWRAP=OFF \
    -DWITH_LTO=ON \
    -DWITH_JEMALLOC=ON \
    -DWITH_READLINE=ON \
    -DWITH_SYSTEMD=yes \
    -DWITH_PROTOBUF=bundled \
    -DWITH_UNIT_TESTS=OFF \
    -DPLUGIN_EXAMPLE=NO \
    -DWITHOUT_EXAMPLE_STORAGE_ENGINE=ON \
    -DPLUGIN_FEDERATED=NO \
    -DWITHOUT_FEDERATED_STORAGE_ENGINE=ON \
    -DPLUGIN_FEEDBACK=NO \
    -DCMAKE_C_FLAGS="${CFLAGS}" \
    -DCMAKE_C_LINK_FLAGS="${LDFLAGS}" \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS} -DU_DEFINE_FALSE_AND_TRUE=1" \
    -DCMAKE_CXX_LINK_FLAGS="${LDFLAGS}" \
    -DDEFAULT_CHARSET=utf8mb4 \
    -DDEFAULT_COLLATION=utf8mb4_unicode_ci \
    -DWITH_BOOST="../${pkgname}-${pkgver}/boost"
  make
}

check() {
  cd build/mysql-test

  # Takes *really* long, so disabled by default.
  # ./mtr --parallel=5 --mem --force --max-test-fail=0
}

package_libmysqlclient(){
  pkgdesc="MySQL client libraries"
  depends=('libsasl' 'zlib' 'zstd')
  conflicts=('libmariadbclient' 'mariadb-libs')
  provides=("libmariadbclient=${pkgver}" "libmysqlclient=${pkgver}" "mariadb-libs=${pkgver}")

  cd build
  for dir in include libmysql libservices
  do
    make -C "${dir}" DESTDIR="${pkgdir}" install
  done

  install -m 700 -d "${pkgdir}/var/lib/mysql"
  install -m 644 -D "${srcdir}/my-default.cnf" "${pkgdir}/etc/mysql/my.cnf.default"
  install -m 644 -D "${srcdir}/${pkgbase}-${pkgver}/support-files/mysql.m4" "${pkgdir}/usr/share/aclocal/mysql.m4"
}

package_mysql-clients(){
  pkgdesc="MySQL client tools"
  depends=('libmysqlclient' 'zlib' 'openssl' 'jemalloc' 'libedit' 'lz4' 'zstd' 'bash')
  conflicts=('mariadb-clients')
  provides=("mariadb-clients=${pkgver}" "mysql-clients=${pkgver}")

  cd build
  make -C "client" DESTDIR="${pkgdir}" install

  install -m 755 -d "${pkgdir}/usr/bin"
  install -m 755 "runtime_output_directory/mysql_client_test" "${pkgdir}/usr/bin"
  install -m 755 "scripts/mysql_config" "${pkgdir}/usr/bin"

  # install man pages
  install -m 755 -d "${pkgdir}/usr/share/man/man1"
  for man in mysql mysqladmin mysqlcheck mysqldump mysqlimport mysqlshow mysqlslap mysql_config mysql_config_editor
  do
    install -m 644 "${srcdir}/${pkgbase}-${pkgver}/man/${man}.1" "${pkgdir}/usr/share/man/man1/${man}.1"
  done

  # install pkgconfig
  install -m 644 -D "${srcdir}/build/scripts/mysqlclient.pc" "${pkgdir}/usr/lib/pkgconfig/mysqlclient.pc"

  # provided by mysql
  rm "${pkgdir}/usr/bin/mysql_upgrade"
  rm "${pkgdir}/usr/bin/mysqlbinlog"
  rm "${pkgdir}/usr/bin/mysql_migrate_keyring"
  rm "${pkgdir}/usr/bin/mysqlpump"
  rm "${pkgdir}/usr/bin/mysql_secure_installation"
  rm "${pkgdir}/usr/bin/mysql_ssl_rsa_setup"
  rm "${pkgdir}/usr/bin/mysqltest"
}

package_mysql(){
  pkgdesc="Fast SQL database server, community edition"
  backup=("etc/mysql/my.cnf"
          "etc/mysqlrouter/mysqlrouter.conf"
          "etc/logrotate.d/mysqlrouter"
          "etc/conf.d/${pkgname}.conf")
  install="${pkgbase}.install"
  depends=('mysql-clients' 'libsasl' 'zlib' 'jemalloc' 'libaio' 'libtirpc' 'icu'
           'lz4' 'libevent' 'systemd-libs' 'zstd' 'bash')
  conflicts=('mariadb')
  provides=("mariadb=${pkgver}" "mysql=${pkgver}")
  optdepends=('perl-dbd-mysql: for mysqlhotcopy, mysql_convert_table_format, mysql_setpermission, mysqldumpslow')
  options=('emptydirs')

  cd build
  make DESTDIR="${pkgdir}" install

  install -m 644 -D "${srcdir}/my-default.cnf" "${pkgdir}/etc/mysql/my.cnf"
  install -m 755 -d "${pkgdir}/etc/ld.so.conf.d"
  install -m 644 -D "${srcdir}/mysql-ld.so.conf" "${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf"
  install -m 644 -D "${srcdir}/build/packaging/rpm-common/mysqlrouter.conf" "${pkgdir}/etc/mysqlrouter/mysqlrouter.conf"

  # provided by libmysqlclient
  rm "${pkgdir}/usr/bin/mysql_config"
  rm "${pkgdir}/usr/lib/libmysqlclient.a"
  rm "${pkgdir}/usr/lib/libmysqlclient.so"
  rm "${pkgdir}/usr/lib/libmysqlclient.so.21"
  rm "${pkgdir}/usr/lib/libmysqlclient.so.21.2.32"
  rm "${pkgdir}/usr/lib/libmysqlservices.a"
  rm "${pkgdir}/usr/lib/pkgconfig/mysqlclient.pc"
  rmdir "${pkgdir}/usr/lib/pkgconfig"
  rm -r "${pkgdir}/usr/include"
  rm "${pkgdir}/usr/share/mysql/aclocal/mysql.m4"
  rmdir "${pkgdir}/usr/share/mysql/aclocal"

  # provided by mysql-clients
  rm "${pkgdir}/usr/bin/mysql"
  rm "${pkgdir}/usr/bin/mysqladmin"
  rm "${pkgdir}/usr/bin/mysqlcheck"
  rm "${pkgdir}/usr/bin/mysqldump"
  rm "${pkgdir}/usr/bin/mysqlimport"
  rm "${pkgdir}/usr/bin/mysqlshow"
  rm "${pkgdir}/usr/bin/mysqlslap"
  rm "${pkgdir}/usr/bin/mysql_client_test"
  rm "${pkgdir}/usr/bin/mysql_config_editor"
  rm "${pkgdir}/usr/share/man/man1/mysql.1"
  rm "${pkgdir}/usr/share/man/man1/mysqladmin.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlcheck.1"
  rm "${pkgdir}/usr/share/man/man1/mysql_config.1"
  rm "${pkgdir}/usr/share/man/man1/mysql_config_editor.1"
  rm "${pkgdir}/usr/share/man/man1/mysqldump.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlimport.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlshow.1"
  rm "${pkgdir}/usr/share/man/man1/mysqlslap.1"

  # not needed
  rm -r "${pkgdir}/usr/mysql-test"

  # Move somewhere else
  mv "${pkgdir}/usr/LICENSE.router" "${pkgdir}/usr/share/mysql/docs"
  mv "${pkgdir}/usr/README.router" "${pkgdir}/usr/share/mysql/docs"

  # Create environment file
  install -m 644 -D "${srcdir}/mysql.sysconfig" "${pkgdir}/etc/conf.d/${pkgname}.conf"

  # Fix permissions
  chmod 755 "${pkgdir}/usr"

  # Move systemd files
  mv "${pkgdir}/usr/usr/lib/systemd" "${pkgdir}/usr/lib"
  mv "${pkgdir}/usr/usr/lib/tmpfiles.d" "${pkgdir}/usr/lib"
  install -m 755 -d "${pkgdir}/usr/lib/sysusers.d"
  install -m 644 "${srcdir}/systemd-sysusers.conf" "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"

  # Move logrotate files
  install -d -m 755 "${pkgdir}/etc/logrotate.d/"
  mv "${pkgdir}/usr/mysqlrouter-log-rotate" "${pkgdir}/etc/logrotate.d/mysqlrouter"

  # Move docs files
  mv "${pkgdir}/usr/docs/sample_mysqlrouter.conf" "${pkgdir}/usr/share/mysql/docs"
  rmdir "${pkgdir}/usr/docs"

  # Cleanup
  rmdir "${pkgdir}/usr/usr/lib"
  rmdir "${pkgdir}/usr/usr"

  # Arch Linux specific patches:
  #  * enable PrivateTmp for a little bit more security
  #  * force preloading jemalloc for memory management
  #  * fix path to our config
  cd "${pkgdir}"
  patch -Np1 -i "${srcdir}/mysqld_service.patch"
  patch -Np1 -i "${srcdir}/systemd-tmpfiles.patch"
}

