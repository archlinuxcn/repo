# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>

pkgname=libxpresent
pkgver=1.0.0+3+g9d31d21
pkgrel=1
pkgdesc="X Present Extension library"
arch=('i686' 'x86_64')
url="https://gitlab.freedesktop.org/xorg/lib/libxpresent"
license=('custom')
depends=('xorgproto' 'libxfixes' 'libxrandr')
makedepends=('git' 'xorg-util-macros')
_commit=9d31d2162af3b50a6d7c0175d7abc680da9aec76
source=("git+https://gitlab.freedesktop.org/xorg/lib/libxpresent.git#commit=${_commit}")
sha256sums=('SKIP')

pkgver() {
  cd "${pkgname}"
  git describe --long | sed 's/libXpresent-//;s/-/+/g'
}

build() {
  cd "${pkgname}"

  ./autogen.sh --prefix=/usr --disable-dependency-tracking
  # -Wl,--as-needed should come before all libraries
  sed -i -e '/\$CC/s/-shared/\0 -Wl,--as-needed/' libtool
  make
}

package() {
  cd "${pkgname}"

  make DESTDIR="${pkgdir}" install

  install -D -m 0644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
