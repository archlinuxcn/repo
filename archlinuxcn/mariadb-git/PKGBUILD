# Maintainer: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Maintainer: Christian Hesse <mail@eworm.de>

pkgbase=mariadb-git
_pkgbase=mariadb
pkgname=('mariadb-libs-git' 'mariadb-clients-git' 'mariadb-git' 'mytop-git')
pkgdesc='Fast SQL database server, derived from MySQL (GIT version)'
pkgver=10.4.2.r212.g4932aba9217
pkgrel=2
arch=('x86_64')
license=('GPL')
url='https://mariadb.org/'
makedepends=('boost' 'bzip2' 'cmake' 'jemalloc' 'libaio' 'libxml2' 'lz4' 'lzo'
                 'openssl' 'systemd' 'zlib' 'zstd' 'git')
source=("$_pkgbase::git://github.com/MariaDB/server.git"        
        '0001-arch-specific.patch'
        '0002-systemd-sysusers-tmpfiles.patch'
        '0004-do-not-break-main-configuration-with-instantiated-one.patch'
        '0005-fix-galera_recovery-with-fs.protected_regular-enabled.patch')
sha256sums=('SKIP'
            '5a443a403821931ce35759e9583d23cd809b3b5a5df5b8293ac8e33b9c0cbc0f'
            '1cd009b473d5965c7cbe6d48fff272030a2ccdd9c7e67b4f837d03252786a09a'
            'd12806e4f90cc0fc081205dd4c0a5e0e7c455844f04276811b61b57fd24f5545'
            '66e0acac7436fd8925710ef5cc66ba1a8f63a385ce374f01ae83096cc33d97a0')

prepare() {
  cd $_pkgbase/

  # Arch Linux specific patches:
  #  * enable PrivateTmp for a little bit more security
  #  * force preloading jemalloc for memory management
  #  * fix path to our config
  patch -Np1 < ../0001-arch-specific.patch

  # MDEV-17028 Fix glitches with systemd sysusers and tmpfiles:
  #  * Use descriptive file names for sysusers and tmpfiles configuration
  #  * Make systemd-tmpfiles create MYSQL_DATADIR
  # https://github.com/MariaDB/server/pull/530
  patch -Np1 < ../0002-systemd-sysusers-tmpfiles.patch

  # do not break main configuration with instantiated one
  # https://github.com/MariaDB/server/pull/1095
  patch -Np1 < ../0004-do-not-break-main-configuration-with-instantiated-one.patch

  # fix galera_recovery with fs.protected_regular enabled
  # https://github.com/MariaDB/server/pull/1137
  patch -Np1 < ../0005-fix-galera_recovery-with-fs.protected_regular-enabled.patch
}

build() {
  local _cmake_options=(
    # build options
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
    -Wno-dev

    # file paths
    # /etc
    -DINSTALL_SYSCONFDIR=/etc/mysql
    -DINSTALL_SYSCONF2DIR=/etc/mysql/my.cnf.d
    # /run
    -DINSTALL_UNIX_ADDRDIR=/run/mysqld/mysqld.sock
    # /usr
    -DCMAKE_INSTALL_PREFIX=/usr
    # /usr/bin /usr/include
    -DINSTALL_SCRIPTDIR=bin
    -DINSTALL_INCLUDEDIR=include/mysql
    # /usr/lib
    -DINSTALL_PLUGINDIR=lib/mysql/plugin
    -DINSTALL_SYSTEMD_UNITDIR=/usr/lib/systemd/system/
    -DINSTALL_SYSTEMD_SYSUSERSDIR=/usr/lib/sysusers.d/
    -DINSTALL_SYSTEMD_TMPFILESDIR=/usr/lib/tmpfiles.d/
    # /usr/share
    -DINSTALL_SHAREDIR=share
    -DINSTALL_SUPPORTFILESDIR=share/mysql
    -DINSTALL_MYSQLSHAREDIR=share/mysql
    -DINSTALL_DOCREADMEDIR=share/doc/mariadb
    -DINSTALL_DOCDIR=share/doc/mariadb
    -DINSTALL_MANDIR=share/man
    # /var
    -DMYSQL_DATADIR=/var/lib/mysql

    # default settings
    -DDEFAULT_CHARSET=utf8mb4
    -DDEFAULT_COLLATION=utf8mb4_unicode_ci

    # features
    -DENABLED_LOCAL_INFILE=ON
    -DPLUGIN_EXAMPLE=NO
    -DPLUGIN_FEDERATED=NO
    -DPLUGIN_FEEDBACK=NO
    -DWITH_EMBEDDED_SERVER=ON
    -DWITH_EXTRA_CHARSETS=complex
    -DWITH_JEMALLOC=ON
    -DWITH_LIBWRAP=OFF
    -DWITH_PCRE=bundled
    -DWITH_READLINE=ON
    -DWITH_SSL=system
    -DWITH_SYSTEMD=yes
    -DWITH_UNIT_TESTS=OFF
    -DWITH_ZLIB=system
  )

  mkdir build
  cd build

  cmake ../"$_pkgbase" "${_cmake_options[@]}"

  make
}

check() {
  cd build/mysql-test

  # Takes *really* long, so disabled by default.
  #./mtr --parallel=5 --mem --force --max-test-fail=0
}

package_mariadb-libs-git() {
  pkgdesc='MariaDB libraries (GIT version)'
  depends=('bzip2' 'libaio' 'lz4' 'lzo' 'openssl' 'xz' 'zlib' 'krb5')
  conflicts=('libmysqlclient' 'libmariadbclient' 'mariadb-connector-c' 'mariadb-libs')
  provides=('libmariadbclient' 'mariadb-connector-c' 'mariadb-libs')
  replaces=('libmariadbclient')

  cd build

  for dir in libmariadb libmysqld libservices include; do
    make -C "$dir" DESTDIR="$pkgdir" install
  done

  ln -s mariadb_config "$pkgdir"/usr/bin/mysql_config
  install -D -m0644 "$srcdir"/"$_pkgbase"/man/mysql_config.1 "$pkgdir"/usr/share/man/man1/mysql_config.1

  install -D -m0644 support-files/mariadb.pc "$pkgdir"/usr/share/pkgconfig/mariadb.pc
  install -D -m0644 "$srcdir"/"$_pkgbase"/support-files/mysql.m4 "$pkgdir"/usr/share/aclocal/mysql.m4

  cd "$pkgdir"

  # remove static libraries
  rm usr/lib/*.a
  rm usr/lib/mysql/plugin/client_ed25519.so
}

package_mariadb-clients-git() {
  pkgdesc='MariaDB client tools'
  depends=('mariadb-libs-git' 'jemalloc')
  conflicts=('mysql-clients' 'mariadb-clients')
  provides=("mysql-clients=${pkgver}" 'mariadb-clients')

  cd build

  make -C client DESTDIR="$pkgdir" install

  # install man pages
  for man in mysql mysql_plugin mysql_upgrade mysqladmin mysqlbinlog mysqlcheck mysqldump mysqlimport mysqlshow mysqlslap mysqltest; do
    install -D -m0644 "$srcdir"/"$_pkgbase"/man/"$man.1" "$pkgdir"/usr/share/man/man1/"$man.1"
  done
}

package_mariadb-git() {
  pkgdesc='Fast SQL database server, derived from MySQL'
  backup=('etc/mysql/my.cnf'
          'etc/mysql/my.cnf.d/client.cnf'
          'etc/mysql/my.cnf.d/enable_encryption.preset'
          'etc/mysql/my.cnf.d/mysql-clients.cnf'
          'etc/mysql/my.cnf.d/server.cnf')
  install=mariadb.install
  depends=("mariadb-clients-git" 'inetutils' 'systemd-libs' 'libxml2' 'zstd' 'python')
  optdepends=('galera: for MariaDB cluster with Galera WSREP'
              'perl-dbd-mysql: for mysqlhotcopy, mysql_convert_table_format and mysql_setpermission')
  conflicts=('mysql' 'mariadb')
  provides=("mysql=$pkgver" 'mariadb')
  options=('emptydirs')

  cd build

  make DESTDIR="$pkgdir" install

  cd "$pkgdir"

  # no SysV init, please!
  rm -r etc/mysql/{init.d,logrotate.d}
  rm usr/bin/rcmysql
  rm usr/share/mysql/{binary-configure,mysql{,d_multi}.server}

  # link service files with old name for compatibility
  ln -s mariadb.service usr/lib/systemd/system/mysqld.service
  ln -s mariadb@.service usr/lib/systemd/system/mysqld@.service

  # move to proper licenses directories
  install -d usr/share/licenses/mariadb
  mv usr/share/doc/mariadb/COPYING* usr/share/licenses/mariadb/

  # move it where one might look for it
  mv usr/share/{groonga{,-normalizer-mysql},doc/mariadb/}

  # already installed to real systemd unit directory or useless
  rm -r usr/share/mysql/systemd/
  rm -r usr/lib/systemd/system/mariadb@bootstrap.service.d

  # provided by mariadb-libs
  rm usr/bin/mariadb_config
  rm usr/bin/mysql_config
  rm -r usr/include/
  rm usr/share/man/man1/mysql_config.1
  rm -r usr/share/{aclocal,pkgconfig}
  rm usr/lib/lib*
  rm usr/lib/mysql/plugin/{auth_gssapi_client,caching_sha2_password,dialog,mysql_clear_password,sha256_password}.so
  rm -r usr/lib/pkgconfig/

  # provided by mariadb-clients
  rm usr/bin/{mysql,mysql_plugin,mysql_upgrade,mysqladmin,mysqlbinlog,mysqlcheck,mysqldump,mysqlimport,mysqlshow,mysqlslap,mysqltest}
  rm usr/share/man/man1/{mysql,mysql_plugin,mysql_upgrade,mysqladmin,mysqlbinlog,mysqlcheck,mysqldump,mysqlimport,mysqlshow,mysqlslap,mysqltest}.1

  # provided by mytop
  rm usr/bin/mytop

  # not needed
  rm -r usr/{data,mysql-test,sql-bench}
  rm usr/share/man/man1/mysql-test-run.pl.1
}

package_mytop-git() {
  pkgdesc='Top clone for MariaDB'
  depends=('perl' 'perl-dbd-mysql' 'perl-term-readkey')
  provides=('mytop')
  conflicts=('mytop')

  cd build

  install -D -m0755 scripts/mytop "$pkgdir"/usr/bin/mytop
}
