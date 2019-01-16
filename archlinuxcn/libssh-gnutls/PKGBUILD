# Maintainer: Fredy García <frealgagu at gmail dot com>

pkgbase=libssh-gnutls
pkgname=(${pkgbase} ${pkgbase}-docs)
pkgver=0.8.6
pkgrel=1
pkgdesc="Library for accessing ssh client services through C libraries - compiled with gnutls (libgcrypt), documentation for libssh"
arch=("x86_64")
url="http://www.libssh.org/"
license=("LGPL")
makedepends=("cmake" "cmocka" "doxygen" "python")
source=("https://www.libssh.org/files/${pkgver%.*}/${pkgname%-gnutls}-${pkgver}.tar.xz"{,.asc})
sha256sums=("1046b95632a07fc00b1ea70ee683072d0c8a23f544f4535440b727812002fd01" "SKIP")
validpgpkeys=("8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D") # Andreas Schneider <asn@cryptomilk.org>

prepare() {
  cd "${srcdir}"
  mkdir -p "${srcdir}/build"
}

build() {
  cd "${srcdir}/build"
  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DWITH_GSSAPI=OFF \
    -DWITH_GCRYPT=ON \
    -DUNIT_TESTING=ON \
    "${srcdir}/${pkgname%-gnutls}-${pkgver}"
  make
  make docs
}

check() {
  cd "${srcdir}/build"
  make test
}

package_libssh-gnutls() {
  pkgdesc="Library for accessing ssh client services through C libraries - compiled with gnutls (libgcrypt)"
  arch=("${CARCH}")
  provides=("${pkgname/-gnutls/}")
  conflicts=("${pkgname/-gnutls/}")
  depends=("libgcrypt" "zlib")

  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}" install
}

package_libssh-gnutls-docs() {
  pkgdesc="Documentation for libssh"
  arch=("any")
  provides=("${pkgname/-gnutls/}")
  conflicts=("${pkgname/-gnutls/}")

  mkdir -p "${pkgdir}/usr/share/doc/libssh"
  cp -r "${srcdir}/build/doc/html" "${pkgdir}/usr/share/doc/libssh"
}
