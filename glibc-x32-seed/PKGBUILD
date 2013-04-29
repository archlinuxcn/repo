pkgname=glibc-x32-seed
pkgver=0.1.0
pkgrel=1
pkgdesc="The temporary missing Glibc header file for x32 (stubs-x32.h)"
arch=(x86_64)
license=('GPL')
url="http://sourceware.org/glibc/wiki/x32"

package() {
  mkdir -p ${pkgdir}/usr/include/gnu
  ln -s /usr/include/gnu/stubs-64.h ${pkgdir}/usr/include/gnu/stubs-x32.h
}

