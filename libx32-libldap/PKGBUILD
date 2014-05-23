# $Id: PKGBUILD 106866 2014-03-09 12:49:20Z bpiotrowski $
# Upstream Maintainer:
# Contributor: Judd Vinet <jvinet@zeroflux.org>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libldap
pkgname=libx32-$_pkgbasename
pkgver=2.4.39
pkgrel=1
pkgdesc="Lightweight Directory Access Protocol (LDAP) client libraries (x32 ABI)"
arch=('x86_64')
license=('custom')
url="http://www.openldap.org/"
depends=('libx32-openssl' $_pkgbasename)
makedepends=(gcc-multilib)
source=("ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-${pkgver}.tgz"
        'ntlm.patch')
md5sums=('b0d5ee4b252c841dec6b332d679cf943'
         '4258ddbef923d1f29f2843bc050f8c56')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd ${srcdir}/openldap-${pkgver}

  patch -Np1 -i ${srcdir}/ntlm.patch

  ./configure --prefix=/usr \
              --libexecdir=/usr/sbin \
              --sysconfdir=/etc \
	      --mandir=/usr/share/man \
              --localstatedir=/var/lib/openldap \
              --enable-crypt --enable-dynamic \
              --with-threads --disable-wrappers \
	      --disable-spasswd --without-cyrus-sasl \
	      --disable-bdb --disable-hdb --libdir=/usr/libx32

  cd include
  make

  cd ../libraries
  make depend
  make

}

package() {
  cd ${srcdir}/openldap-${pkgver}

  cd include
  make DESTDIR=${pkgdir} install

  cd ../libraries
  make DESTDIR=${pkgdir} install

  rm -rf "${pkgdir}"/usr/{include,share,bin} "$pkgdir/etc"
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
