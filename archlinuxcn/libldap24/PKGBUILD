# Maintainer:

pkgname=libldap24
pkgver=2.4.59
pkgrel=4
pkgdesc="Lightweight Directory Access Protocol (LDAP) client libraries"
arch=('x86_64')
url="https://www.openldap.org/"
license=('custom')
makedepends=('libtool' 'libsasl' 'e2fsprogs' 'util-linux' 'chrpath' 'unixodbc' 'libsodium')
depends=(libsasl openssl)
options=('!makeflags' 'emptydirs')
source=(https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-${pkgver}.tgz
    libldap-symbol-versions.patch
    macro.patch)
sha256sums=('99f37d6747d88206c470067eda624d5e48c1011e943ec0ab217bae8712e22f34'
            'c7862f6605450b15aff1f967bd17d57470d6d9fa4242c6306499173f0e67938c'
            'a76edf2c9e75f9914d81ee6247e58f1948ae6a6a1028f6d9f717a83a549eb544')

prepare() {
  cd openldap-${pkgver}
  sed -i 's|-m 644 $(LIBRARY)|-m 755 $(LIBRARY)|' libraries/{liblber,libldap,libldap_r}/Makefile.in
  sed -i 's|#define LDAPI_SOCK LDAP_RUNDIR LDAP_DIRSEP "run" LDAP_DIRSEP "ldapi"|#define LDAPI_SOCK LDAP_DIRSEP "run" LDAP_DIRSEP "openldap" LDAP_DIRSEP "ldapi"|' include/ldap_defaults.h
  sed -i 's|%LOCALSTATEDIR%/run|/run/openldap|' servers/slapd/slapd.{conf,ldif}
  sed -i 's|-$(MKDIR) $(DESTDIR)$(localstatedir)/run|-$(MKDIR) $(DESTDIR)/run/openldap|' servers/slapd/Makefile.in
  patch -p1 -i ../macro.patch
  patch -p1 -i ../libldap-symbol-versions.patch
}

build() {
  cd openldap-${pkgver}
  autoupdate
  autoconf
  CFLAGS="${CFLAGS} -DLDAP_CONNECTIONLESS -Wno-implicit-function-declaration -Wno-incompatible-pointer-types -std=gnu17" ./configure --prefix=/usr --libexecdir=/usr/lib \
    --sysconfdir=/etc --localstatedir=/var/lib/openldap --sbindir=/usr/bin \
    --enable-dynamic --enable-syslog --enable-ipv6 --enable-local \
    --enable-crypt --enable-spasswd --enable-modules \
    --enable-backends --disable-ndb --enable-overlays=mod \
    --with-cyrus-sasl --with-threads --disable-bdb --disable-hdb --enable-static=no

  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make

  #make -C contrib/slapd-modules/nssov OPT="$CFLAGS $CPPFLAGS" prefix=/usr libexecdir=/usr/lib sysconfdir=/etc/openldap
  #make -C contrib/slapd-modules/autogroup OPT="$CFLAGS $CPPFLAGS" prefix=/usr libexecdir=/usr/lib sysconfdir=/etc/openldap
  #make -C contrib/slapd-modules/lastbind OPT="$CFLAGS $CPPFLAGS" prefix=/usr libexecdir=/usr/lib sysconfdir=/etc/openldap
  #make -C contrib/slapd-modules/passwd/sha2 OPT="$CFLAGS $CPPFLAGS" prefix=/usr libexecdir=/usr/lib sysconfdir=/etc/openldap
  #make -C contrib/slapd-modules/passwd/argon2 OPT="$CFLAGS $CPPFLAGS" prefix=/usr libexecdir=/usr/lib sysconfdir=/etc/openldap
}

package() {
  cd openldap-${pkgver}
  for dir in libraries; do
    pushd ${dir}
    make DESTDIR="${pkgdir}" install
    popd
  done

  # get rid of duplicate default conf files
  rm "${pkgdir}"/etc/openldap/*.default

  rm "${pkgdir}"/usr/lib/{liblber.so,libldap.so}

  rm "${pkgdir}"/etc/openldap/ldap.conf

  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
