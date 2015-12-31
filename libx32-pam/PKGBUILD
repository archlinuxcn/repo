# $Id: PKGBUILD 143656 2015-10-11 15:23:01Z alucryd $
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: jtts <jussaar@mbnet.fi>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: Janax <janax99@yahoo.com>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com> 

pkgname=libx32-pam
pkgver=1.2.1
pkgrel=1.1
pkgdesc='PAM (Pluggable Authentication Modules) (x32 ABI)'
arch=('x86_64')
url='http://linux-pam.org'
license=('GPL2')
depends=('libx32-cracklib' 'libx32-libtirpc' 'pam')
makedepends=('gcc-multilib-x32' 'libx32-flex')
source=("http://linux-pam.org/library/Linux-PAM-${pkgver}.tar.bz2"
        'https://sources.archlinux.org/other/pam_unix2/pam_unix2-2.9.1.tar.bz2'
        'pam_unix2-glibc216.patch')
sha256sums=('342b1211c0d3b203a7df2540a5b03a428a087bd8a48c17e49ae268f992b334d9'
            '3315747699fece4e1cc5771885d243b3e017c4c4ca1326e86228d590a840e955'
            '6644c5cff46878c65bdc77977becbeda392675702264bfcc7c610a45a9982574')
options=('!emptydirs')

prepare () {
  cd pam_unix2-2.9.1

  patch -Np1 -i ../pam_unix2-glibc216.patch
}

build() {
  cd Linux-PAM-${pkgver}

  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'
  
  ./configure \
    --prefix='/usr' \
    --libdir='/usr/libx32' \
    --sbindir='/usr/bin' \
    --disable-db
  make

  cd ../pam_unix2-2.9.1

  export CFLAGS="$CFLAGS -I"${srcdir}"/Linux-PAM-${pkgver}/libpam/include/"
  export LDFLAGS="$LDFLAGS -L"${srcdir}"/Linux-PAM-${pkgver}/libpam/.libs/"

  ./configure --prefix='/usr' \
              --libdir='/usr/libx32' \
              --sbindir='/usr/bin'
  make
}

package() {
  cd Linux-PAM-${pkgver}

  make DESTDIR="${pkgdir}" SCONFIGDIR='/etc/security' install
  rm -rf "${pkgdir}"/{etc,usr/{include,share,bin}}

  cd ../pam_unix2-2.9.1

  install -m 644 src/pam_unix2.so "${pkgdir}"/usr/libx32/security/

  cd "${pkgdir}"/usr/libx32/security

  ln -s pam_unix.so pam_unix_acct.so
  ln -s pam_unix.so pam_unix_auth.so
  ln -s pam_unix.so pam_unix_passwd.so
  ln -s pam_unix.so pam_unix_session.so
}

# vim: ts=2 sw=2 et:
