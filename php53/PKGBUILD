# $Id$
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgbase=php53
pkgname=('php53'
         'php53-cgi'
         'php53-apache'
         'php53-fpm'
         'php53-embed'
         'php53-pear'
         'php53-enchant'
         'php53-gd'
         'php53-imap'
         'php53-intl'
         'php53-ldap'
         'php53-mcrypt'
         'php53-mssql'
         'php53-odbc'
         'php53-pgsql'
         'php53-pspell'
         'php53-snmp'
         'php53-sqlite'
         'php53-tidy'
         'php53-xsl')
pkgver=5.3.29
_suhosinver=5.3.9-0.9.10
pkgrel=4
arch=('i686' 'x86_64')
license=('PHP')
url='http://www.php.net'
makedepends=('apache' 'c-client' 'postgresql-libs' 'libldap' 'postfix'
             'sqlite' 'unixodbc' 'net-snmp' 'libzip' 'enchant' 'file' 'freetds'
             'libmcrypt' 'tidyhtml' 'aspell' 'libltdl' 'libpng' 'libjpeg' 'icu'
             'curl' 'libxslt' 'openssl' 'bzip2' 'db' 'gmp' 'freetype2' 'sed')
source=("http://www.php.net/distributions/${pkgbase%53}-${pkgver}.tar.bz2"
        "http://download.suhosin.org/suhosin-patch-${_suhosinver}.patch.gz"
        php.ini.patch apache.conf php-fpm.conf.in.patch
        logrotate.d.php-fpm suhosin.patch freetype-path.patch
        CVE-2014-3587.patch CVE-2014-3597.patch CVE-2014-3668.patch
        CVE-2014-3669.patch CVE-2014-3670.patch curl_embedded_null.patch
        CVE-2014-8142.patch CVE-2015-0231.patch CVE-2014-9705.patch
        CVE-2015-0273.patch CVE-2015-2301.patch CVE-2015-2305.patch
        CVE-2015-2783.patch CVE-2015-2787.patch CVE-2015-3330.patch
        CVE-2015-3329.patch)

build() {
    phpconfig="--srcdir=../${pkgbase%53}-${pkgver} \
        --prefix=/usr \
        --sysconfdir=/etc/php \
        --localstatedir=/var \
        --with-layout=GNU \
        --with-config-file-path=/etc/php \
        --with-config-file-scan-dir=/etc/php/conf.d \
        --enable-inline-optimization \
        --disable-debug \
        --disable-rpath \
        --disable-static \
        --enable-shared \
        --mandir=/usr/share/man \
        --without-pear \
        "

    phpextensions="--enable-bcmath=shared \
        --enable-calendar=shared \
        --enable-dba=shared \
        --enable-exif=shared \
        --enable-ftp=shared \
        --enable-gd-native-ttf \
        --enable-intl=shared \
        --enable-json=shared \
        --enable-mbregex \
        --enable-mbstring \
        --enable-pdo \
        --enable-phar=shared \
        --enable-posix=shared \
        --enable-session \
        --enable-shmop=shared \
        --enable-soap=shared \
        --enable-sockets=shared \
        --enable-sqlite-utf8 \
        --enable-sysvmsg=shared \
        --enable-sysvsem=shared \
        --enable-sysvshm=shared \
        --enable-xml \
        --enable-zip=shared \
        --with-bz2=shared \
        --with-curl=shared \
        --with-enchant=shared,/usr \
        --with-freetype-dir=shared,/usr \
        --with-gd=shared \
        --with-gdbm=shared \
        --with-gettext=shared \
        --with-gmp=shared \
        --with-iconv=shared \
        --with-icu-dir=/usr \
        --with-imap-ssl=shared,/usr \
        --with-imap=shared,/usr \
        --with-jpeg-dir=shared,/usr \
        --with-kerberos=/usr \
        --with-ldap=shared \
        --with-ldap-sasl \
        --with-mcrypt=shared \
        --with-mhash \
        --with-mssql=shared \
        --with-mysql-sock=/var/run/mysqld/mysqld.sock \
        --with-mysql=shared,mysqlnd \
        --with-mysqli=shared,mysqlnd \
        --with-openssl=shared \
        --with-pcre-regex=/usr \
        --with-pdo-mysql=shared,mysqlnd \
        --with-pdo-odbc=shared,unixODBC,/usr \
        --with-pdo-pgsql=shared \
        --with-pdo-sqlite=shared,/usr \
        --with-pgsql=shared \
        --with-png-dir=shared,/usr \
        --with-pspell=shared \
        --with-regex=php \
        --with-snmp=shared \
        --with-sqlite3=shared,/usr \
        --with-sqlite=shared \
        --with-tidy=shared \
        --with-unixODBC=shared,/usr \
        --with-xmlrpc=shared \
        --with-xsl=shared \
        --with-zlib \
        --without-db2 \
        --without-db3 \
        "

    EXTENSION_DIR=/usr/lib/php/modules
    export EXTENSION_DIR
    PEAR_INSTALLDIR=/usr/share/pear
    export PEAR_INSTALLDIR
    
    # -D_FORTIFY_SOURCE=2 will generate a warning, which will fail the configure script
    unset CPPFLAGS

    msg "Fix the suhosin patch"
    patch -l -i ${srcdir}/suhosin.patch
    sed -i 's/1997-2004/1997-2014/g' ${srcdir}/suhosin-patch-${_suhosinver}.patch
    sed -i 's/1997-2012/1997-2014/g' ${srcdir}/suhosin-patch-${_suhosinver}.patch

    cd ${srcdir}/${pkgbase%53}-${pkgver}

    # TODO: some doesn't apply
    msg "Applying security patches (from Ubuntu)"
    # patch -p1 -i ../CVE-2014-3587.patch
    # patch -p1 -i ../CVE-2014-3597.patch
    patch -p1 -i ../CVE-2014-3668.patch
    patch -p1 -i ../CVE-2014-3669.patch
    patch -p1 -i ../CVE-2014-3670.patch
    patch -p1 -i ../curl_embedded_null.patch
    patch -p1 -i ../CVE-2014-8142.patch
    patch -p1 -i ../CVE-2015-0231.patch
    patch -p1 -i ../CVE-2014-9705.patch
    # patch -p1 -i ../CVE-2015-0273.patch
    patch -p1 -i ../CVE-2015-2301.patch
    patch -p1 -i ../CVE-2015-2305.patch
    patch -p1 -i ../CVE-2015-2783.patch
    patch -p1 -i ../CVE-2015-2787.patch
    patch -p1 -i ../CVE-2015-3330.patch
    patch -p1 -i ../CVE-2015-3329.patch

    msg "Applying suhosin patch"
    patch -F3 -p1 -i ${srcdir}/suhosin-patch-${_suhosinver}.patch

    msg "Adjust paths"
    patch -p0 -i ${srcdir}/php.ini.patch
    patch -p0 -i ${srcdir}/php-fpm.conf.in.patch
    patch -p1 -i ${srcdir}/freetype-path.patch

    # To workaround c-client linking problem
    export IMAP_SHARED_LIBADD="-lssl"

    # php
    mkdir ${srcdir}/build-php
    cd ${srcdir}/build-php
    ln -s ../${pkgbase%53}-${pkgver}/configure
    ./configure ${phpconfig} \
        --disable-cgi \
        --with-readline \
        --enable-pcntl \
        ${phpextensions}
    make

    # cgi and fcgi
    # reuse the previous run; this will save us a lot of time
    cp -a ${srcdir}/build-php ${srcdir}/build-cgi
    cd ${srcdir}/build-cgi
    ./configure ${phpconfig} \
        --disable-cli \
        --enable-cgi \
        ${phpextensions}
    make

    # apache
    cp -a ${srcdir}/build-php ${srcdir}/build-apache
    cd ${srcdir}/build-apache
    ./configure ${phpconfig} \
        --disable-cli \
        --with-apxs2 \
        ${phpextensions}
    make

    # fpm
    cp -a ${srcdir}/build-php ${srcdir}/build-fpm
    cd ${srcdir}/build-fpm
    ./configure ${phpconfig} \
        --disable-cli \
        --enable-fpm \
        --with-fpm-user=http \
        --with-fpm-group=http \
        ${phpextensions}
    make

    # embed
    cp -a ${srcdir}/build-php ${srcdir}/build-embed
    cd ${srcdir}/build-embed
    ./configure ${phpconfig} \
        --disable-cli \
        --enable-embed=shared \
        ${phpextensions}
    make

    # pear
    cp -a ${srcdir}/build-php ${srcdir}/build-pear
    cd ${srcdir}/build-pear
    ./configure ${phpconfig} \
        --disable-cgi \
        --with-readline \
        --enable-pcntl \
        --with-pear \
        ${phpextensions}
    make
}

# check() {
#     cd ${srcdir}/build-php
#     make test
# }

package_php53() {
    pkgdesc='An HTML-embedded scripting language - Legacy 5.3 version'
    depends=('pcre' 'libxml2' 'bzip2' 'curl')
    provides=('php' 'php-fileinfo' 'php-gmp' 'php-curl')
    conflicts=('php' 'php-fileinfo' 'php-gmp' 'php-curl')
    backup=('etc/php/php.ini')

    cd ${srcdir}/build-php
    make -j1 INSTALL_ROOT=${pkgdir} install
    install -d -m755 ${pkgdir}/usr/share/pear
    # install php.ini
    install -D -m644 ${srcdir}/${pkgbase%53}-${pkgver}/php.ini-production ${pkgdir}/etc/php/php.ini
    install -d -m755 ${pkgdir}/etc/php/conf.d/

    # remove static modules
    rm -f ${pkgdir}/usr/lib/php/modules/*.a
    # remove modules provided by sub packages
    rm -f ${pkgdir}/usr/lib/php/modules/{enchant,gd,imap,intl,ldap,mcrypt,mssql,odbc,pdo_odbc,pgsql,pdo_pgsql,pspell,snmp,sqlite3,pdo_sqlite,tidy,xsl}.so
    # remove empty directory
    rmdir ${pkgdir}/usr/include/php/include
}

package_php53-cgi() {
    pkgdesc='CGI and FCGI SAPI for PHP'
    depends=('php53')
    conflicts=('php-cgi')
    provides=('php-cgi')

    install -D -m755 ${srcdir}/build-cgi/sapi/cgi/php-cgi ${pkgdir}/usr/bin/php-cgi
}

package_php53-apache() {
    pkgdesc='Apache SAPI for PHP'
    depends=('php53' 'apache')
    conflicts=('php-apache')
    provides=('php-apache')
    backup=('etc/httpd/conf/extra/php5_module.conf')

    install -D -m755 ${srcdir}/build-apache/libs/libphp5.so ${pkgdir}/usr/lib/httpd/modules/libphp5.so
    install -D -m644 ${srcdir}/apache.conf ${pkgdir}/etc/httpd/conf/extra/php5_module.conf
}

package_php53-fpm() {
    pkgdesc='FastCGI Process Manager for PHP'
    depends=('php53')
    conflicts=('php-fpm')
    provides=('php-fpm')
    backup=('etc/php/php-fpm.conf')

    install -D -m755 ${srcdir}/build-fpm/sapi/fpm/php-fpm ${pkgdir}/usr/bin/php-fpm
    install -D -m644 ${srcdir}/build-fpm/sapi/fpm/php-fpm.8 ${pkgdir}/usr/share/man/man8/php-fpm.8
    install -D -m644 ${srcdir}/build-fpm/sapi/fpm/php-fpm.conf ${pkgdir}/etc/php/php-fpm.conf
    install -D -m644 ${srcdir}/logrotate.d.php-fpm ${pkgdir}/etc/logrotate.d/php-fpm
    install -d -m755 ${pkgdir}/etc/php/fpm.d
}

package_php53-embed() {
    pkgdesc='Embed SAPI for PHP'
    depends=('php53')
    conflicts=('php-embed')
    provides=('php-embed')

    install -D -m755 ${srcdir}/build-embed/libs/libphp5.so ${pkgdir}/usr/lib/libphp5.so
    install -D -m644 ${srcdir}/${pkgbase%53}-${pkgver}/sapi/embed/php_embed.h ${pkgdir}/usr/include/php/sapi/embed/php_embed.h
}

package_php53-pear() {
    pkgdesc='PHP Extension and Application Repository'
    depends=('php53')
    conflicts=('php-pear')
    provides=('php-pear')
    backup=('etc/php/pear.conf')

    cd ${srcdir}/build-pear
    make -j1 install-pear INSTALL_ROOT=${pkgdir}
    local i
    while read i; do
        [ ! -e "$i" ] || rm -rf "$i"
    done < <(find ${pkgdir} -name '.*')
}

package_php53-enchant() {
    depends=('php53' 'enchant')
    conflicts=('php-enchant')
    provides=('php-enchant')
    pkgdesc='enchant module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/enchant.so ${pkgdir}/usr/lib/php/modules/enchant.so
}

package_php53-gd() {
    depends=('php53' 'libpng' 'libjpeg' 'freetype2')
    conflicts=('php-gd')
    provides=('php-gd')
    pkgdesc='gd module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/gd.so ${pkgdir}/usr/lib/php/modules/gd.so
}

package_php53-imap() {
    depends=('php53' 'c-client')
    conflicts=('php-imap')
    provides=('php-imap')

    install -D -m755 ${srcdir}/build-php/modules/imap.so ${pkgdir}/usr/lib/php/modules/imap.so
}

package_php53-intl() {
    depends=('php53' 'icu')
    conflicts=('php-intl')
    provides=('php-intl')
    pkgdesc='intl module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/intl.so ${pkgdir}/usr/lib/php/modules/intl.so
}

package_php53-ldap() {
    depends=('php53' 'libldap')
    conflicts=('php-ldap')
    provides=('php-ldap')
    pkgdesc='ldap module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/ldap.so ${pkgdir}/usr/lib/php/modules/ldap.so
}

package_php53-mcrypt() {
    depends=('php53' 'libmcrypt' 'libltdl')
    conflicts=('php-mcrypt')
    provides=('php-mcrypt')
    pkgdesc='mcrypt module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/mcrypt.so ${pkgdir}/usr/lib/php/modules/mcrypt.so
}

package_php53-mssql() {
    depends=('php53' 'freetds')
    conflicts=('php-mssql')
    provides=('php-mssql')
    pkgdesc='mssql module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/mssql.so ${pkgdir}/usr/lib/php/modules/mssql.so
}

package_php53-odbc() {
    depends=('php53' 'unixodbc')
    conflicts=('php-odbc')
    provides=('php-odbc')
    pkgdesc='ODBC modules for PHP'
    install -D -m755 ${srcdir}/build-php/modules/odbc.so ${pkgdir}/usr/lib/php/modules/odbc.so
    install -D -m755 ${srcdir}/build-php/modules/pdo_odbc.so ${pkgdir}/usr/lib/php/modules/pdo_odbc.so
}

package_php53-pgsql() {
    depends=('php53' 'postgresql-libs')
    conflicts=('php-pgsql')
    provides=('php-pgsql')
    pkgdesc='PostgreSQL modules for PHP'
    install -D -m755 ${srcdir}/build-php/modules/pgsql.so ${pkgdir}/usr/lib/php/modules/pgsql.so
    install -D -m755 ${srcdir}/build-php/modules/pdo_pgsql.so ${pkgdir}/usr/lib/php/modules/pdo_pgsql.so
}

package_php53-pspell() {
    depends=('php53' 'aspell')
    conflicts=('php-aspell')
    provides=('php-aspell')
    pkgdesc='pspell module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/pspell.so ${pkgdir}/usr/lib/php/modules/pspell.so
}

package_php53-snmp() {
    depends=('php53' 'net-snmp')
    conflicts=('php-snmp')
    provides=('php-snmp')
    pkgdesc='snmp module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/snmp.so ${pkgdir}/usr/lib/php/modules/snmp.so
}

package_php53-sqlite() {
    depends=('php53' 'sqlite')
    conflicts=('php-sqlite')
    provides=('php-sqlite')
    pkgdesc='sqlite module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/sqlite3.so ${pkgdir}/usr/lib/php/modules/sqlite3.so
    install -D -m755 ${srcdir}/build-php/modules/pdo_sqlite.so ${pkgdir}/usr/lib/php/modules/pdo_sqlite.so
}

package_php53-tidy() {
    depends=('php53' 'tidyhtml')
    conflicts=('php-tidy')
    provides=('php-tidy')
    pkgdesc='tidy module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/tidy.so ${pkgdir}/usr/lib/php/modules/tidy.so
}

package_php53-xsl() {
    depends=('php53' 'libxslt')
    conflicts=('php-xsl')
    provides=('php-xsl')
    pkgdesc='xsl module for PHP'
    install -D -m755 ${srcdir}/build-php/modules/xsl.so ${pkgdir}/usr/lib/php/modules/xsl.so
}

sha1sums=('6e9e492c6d5853d063ddb9a4dbef60b8e5d87444'
          '7b9ef5c3e0831154df0d6290aba0989ca90138ed'
          '462927954b4074487b46722b0442185100def240'
          '82776db01f70b9186ba455de22eb06fe193f1d30'
          'ea9a9101b9678a8461d9dddfc0df2a4412a4cb5d'
          'b6a661523535a8e7e60d4a0c054d8f6066edf63e'
          '4d9fea0b7ab856c59ddbf722fe6c95b8e479af9b'
          '8f19ee0e351aa2cdc9b110db4e33b4c8f6131b12'
          'b5caa85fd1b76a3ece056ab5441852330989640b'
          '9f2aa7c2514cb66204f9f5c3dc5f8ebdda238c78'
          '4672c18ece397b2f99ad0c992f61220e210b2dc1'
          '454e96af5cab1f649fceca61c0afb46ae73179f5'
          '2f368143bcdaae4659a65103ffdeb71cac12c5cf'
          'ede78d11b7d4d6c304253bfd358607e160a3918a'
          'e97ea93d37ffbf6c3025281202d2e807facb4e7e'
          '0ab48f282d62058318d08c44607aac89912f78d6'
          'b535103d79ba9791c22a841d5d72497dec3dd93d'
          '7cb38769807eb7d35ff7f3eaf1cce408d8ad2676'
          '066fe3a84e1aabaf45afe26470cd769b9e3ab79a'
          '4968abe76ab18c15f85111b3e78dba0059f948ce'
          '18e3f12ad04adf4cc59aa5862628ab0d032c76ef'
          '4d9551ec6c2462cde45d0e556edf6d9e792c15b4'
          '248dc92602721c193f3906f3eb7d98cd5499ba40'
          '40fc97494110e9b312ea0f5bade8aa0b7043f40e')

# Fix for AUR
pkgdesc='An HTML-embedded scripting language - Legacy 5.3 version'
