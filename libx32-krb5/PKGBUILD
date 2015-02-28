# $Id: PKGBUILD 127768 2015-02-16 02:18:22Z fyan $
# Maintainer: Florian Pritz <flo@xinu.at>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=krb5
pkgname=libx32-$_pkgbasename
pkgver=1.13.1
pkgrel=1.1
pkgdesc="The Kerberos network authentication system (x32 ABI)"
arch=('x86_64')
url="http://web.mit.edu/kerberos/"
license=('custom')
depends=('libx32-e2fsprogs' 'libx32-libldap' 'libx32-keyutils' "$_pkgbasename")
makedepends=('perl' 'gcc-multilib-x32' 'bison')
source=("http://web.mit.edu/kerberos/dist/${_pkgbasename}/1.13/${_pkgbasename}-${pkgver}-signed.tar"
        krb5-config_LDFLAGS.patch
        krb5-1.13.1-x32.patch)
sha1sums=('2832695845d6c4cb0e7a622df4885f18acbd94cf'
          'f125824ed37f31e6fd2fdb6a437be8ff1c3700ab'
          '928c1367fd48e055fa4ffcad01fd70d1beea22af')
options=('!emptydirs')

prepare() {
   tar zxvf ${_pkgbasename}-${pkgver}.tar.gz
   cd "${srcdir}/${_pkgbasename}-${pkgver}"

   # cf https://bugs.gentoo.org/show_bug.cgi?id=448778
   patch -p1 -i "${srcdir}"/krb5-config_LDFLAGS.patch

   # x32
   patch -p1 -i "${srcdir}"/krb5-1.13.1-x32.patch
}

build() {
   cd "${srcdir}/${_pkgbasename}-${pkgver}/src"

   export CC="gcc -mx32"
   export CXX="g++ -mx32"
   export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"
   export PYTHON="/usr/bin/python2-x32"

   export CFLAGS+=" -fPIC -fno-strict-aliasing -fstack-protector-all"
   export CPPFLAGS+=" -I/usr/include/et"
   ./configure --prefix=/usr \
               --sysconfdir=/etc \
               --localstatedir=/var/lib \
               --libdir=/usr/libx32 \
               --enable-shared \
               --with-system-et \
               --with-system-ss \
               --disable-rpath \
               --without-tcl \
               --enable-dns-for-realm \
               --with-ldap \
               --without-system-verto

   make
}

#check() {
   # We can't do this in the build directory.

   # only works if the hostname is set properly/resolves to something. whatever...
   #cd "${srcdir}/${_pkgbasename}-${pkgver}"
   #make -C src check
#}

package() {
   cd "${srcdir}/${_pkgbasename}-${pkgver}/src"
   make DESTDIR="${pkgdir}" install

   rm -rf "${pkgdir}"/usr/{include,share,bin,sbin}
   mkdir -p "$pkgdir/usr/share/licenses"
   ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
