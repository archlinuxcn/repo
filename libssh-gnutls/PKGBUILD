# Maintainer: Fredy García <frealgagu at gmail dot com>

pkgbase=libssh-gnutls
pkgname=(${pkgbase} ${pkgbase}-docs)
pkgver=0.8.5
pkgrel=1
pkgdesc="Library for accessing ssh client services through C libraries - compiled with gnutls (libgcrypt), documentation for libssh"
arch=("x86_64")
url="http://www.libssh.org/"
license=("LGPL")
makedepends=("cmake" "cmocka" "doxygen" "python")
source=("https://www.libssh.org/files/${pkgver%.*}/${pkgname%-gnutls}-${pkgver}.tar.xz"{,.asc})
sha256sums=("07d2c431240fc88f6b06bcb36ae267f9afeedce2e32f6c42f8844b205ab5a335" "SKIP")
validpgpkeys=("8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D") # Andreas Schneider <asn@cryptomilk.org>

prepare() {
  cd "${srcdir}"
  # disable the test. It is confused by our clean container setup.
  # 'extra-x86-build' uses user 'nobody' that has a record in /etc/passwd file
  # but $HOME envvar is set to '/build'. The test expects that $HOME corresponds to passwd file.
  sed "s/cmocka_unit_test(torture_path_expand_tilde_unix),//" -i "libssh-${pkgver}/tests/unittests/torture_misc.c"
  mkdir -p "${srcdir}/build"
}

build() {
  cd "${srcdir}/build"
  cmake ../${pkgname%-gnutls}-${pkgver} \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DWITH_GSSAPI=OFF \
    -DWITH_GCRYPT=ON \
    -DUNIT_TESTING=ON
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
