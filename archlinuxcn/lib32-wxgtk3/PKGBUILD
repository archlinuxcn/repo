# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=lib32-wxgtk3
pkgver=3.0.5.1
pkgrel=3
pkgdesc='GTK+ implementation of wxWidgets API for GUI'
arch=(x86_64)
url=https://wxwidgets.org
license=(custom:wxWindows)
depends=(
  lib32-expat
  lib32-gtk3
  lib32-libjpeg
  lib32-libpng
  lib32-libsm
  lib32-libtiff
  lib32-zlib
  wxgtk3
)
makedepends=(
  git
  lib32-glu
)
_tag=db9378c1d32e84cf7ca4453932df259471d67dc9
source=(
  git+https://github.com/wxWidgets/wxWidgets.git#tag=${_tag}
  make-abicheck-non-fatal.patch
)
sha256sums=(
  SKIP
  d4c2d070a06eb63f0a018c8cf687589e5ffdec601225b4d16a268ffe390fb58b
)

prepare() {
  cd wxWidgets

  patch -Np1 -i ../make-abicheck-non-fatal.patch

  ./autogen.sh
}

build() {
  cd wxWidgets

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH=/usr/lib32/pkgconfig
  export CFLAGS="-I/usr/include/libtiff32 $CFLAGS"
  export CXXFLAGS="-I/usr/include/libtiff32 $CXXFLAGS"

  ./configure \
    --prefix=/usr \
    --libdir=/usr/lib32 \
    --enable-graphics_ctx \
    --enable-unicode \
    --disable-mediactrl \
    --disable-precomp-headers \
    --disable-webview \
    --with-gtk=3 \
    --with-lib{jpeg,png,tiff}=sys \
    --with-opengl \
    --with-regex=builtin \
    --without-libnotify
  make
  make -C locale allmo
}

package() {
  make DESTDIR="${pkgdir}" -C wxWidgets install
  rm -rf "${pkgdir}"/usr/{bin/{wx-config,wxrc},include,share}
  mv "${pkgdir}"/usr/bin/wxrc{,32}-3.0
  ln -s /usr/bin/wxrc32-3.0 "${pkgdir}"/usr/bin/wxrc32
  ln -s /usr/lib32/wx/config/gtk3-unicode-3.0 "${pkgdir}"/usr/bin/wx-config32

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s wxgtk3 "${pkgdir}"/usr/share/licenses/lib32-wxgtk3
}

# vim: ts=2 sw=2 et:
