# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: lorim <lorimz@gmail.com>

pkgname=libtiff4
pkgver=3.9.7
pkgrel=8
pkgdesc='Library for manipulation of TIFF images - Interface version (SONAME) 4'
arch=(x86_64)
url=http://www.simplesystems.org/libtiff/
license=(custom)
depends=(
  gcc-libs
  jbigkit
  libjpeg-turbo
  zlib
)
makedepends=(
  git
)

source=(
  "git+https://gitlab.com/libtiff/libtiff.git#tag=v${pkgver}"
  "libtiff4-soname.patch"
)
sha256sums=(
  "SKIP"
  "4704379227c530cd76f007fe67638f2d998a074a0af6ca50f063ef720f95b9ba"
)

prepare() {
  cd libtiff

  # Rename 3.9.7 to 4.3.7, 3.6.x was the first release with the unintentional ABI change
  patch -Np1 -i ../libtiff4-soname.patch

  autoreconf -fiv
  ./autogen.sh
}

build() {
  cd libtiff

  ./configure \
    --prefix='/usr'
  make
}

package() {
  make DESTDIR="${pkgdir}" -C libtiff install
  rm -rf "${pkgdir}"/usr/{bin,include,lib/libtiff{,xx}.{a,so},share}
  install -Dm 644 libtiff/COPYRIGHT -t "${pkgdir}"/usr/share/licenses/libtiff4/
}

# vim: ts=2 sw=2 et:
