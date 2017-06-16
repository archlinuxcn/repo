# Maintainer: Geyslan G. Bem <geyslan@gmail.com>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=wxgtk2.8
pkgver=2.8.12.1
pkgrel=6
pkgdesc="GTK+ implementation of wxWidgets API for GUI"
arch=('i686' 'x86_64')
url="http://wxwidgets.org"
license=('custom:wxWindows')
depends=('gtk2' 'gstreamer0.10-base' 'sdl' 'libsm')
makedepends=('gstreamer0.10-base-plugins' 'gconf' 'glu')
provides=("wxgtk2.8=${pkgver}")
conflicts=('wxgtk2.8-light')
options=('!emptydirs')
source=(http://downloads.sourceforge.net/wxpython/wxPython-src-${pkgver}.tar.bz2
        wxGTK-collision.patch
        make-abicheck-non-fatal.patch
        wxGTK-2.8.12.1-r2-gcc6.patch)
sha1sums=('05688dc03d61631750f5904273122bb40a2115f5'
          '75d2292a0058570aa6071b4bee6eef69e47f1208'
          'dfe38650c655395b90bf082b5734c4093508bfa3'
          'f1a3bc30ec8139d97ca239dc1bf6cbc2ceb5c5d9')

prepare() {
  cd wx*-${pkgver}
  patch -p1 -i ../wxGTK-collision.patch

  # C++ ABI check is too strict and breaks with GCC 5.1
  # https://bugzilla.redhat.com/show_bug.cgi?id=1200611
  patch -Np1 -i ../make-abicheck-non-fatal.patch

  # fix gcc6 narrowing error
  # https://bugs.gentoo.org/show_bug.cgi?id=592442
  patch -p1 -i ../wxGTK-2.8.12.1-r2-gcc6.patch
}

build() {
  cd wx*-${pkgver}
  ./configure --prefix=/usr --libdir=/usr/lib --with-gtk=2 --with-opengl --enable-unicode \
    --enable-graphics_ctx  --disable-optimize --enable-mediactrl --with-regex=builtin \
    --with-libpng=sys --with-libxpm=sys --with-libjpeg=sys --with-libtiff=sys \
    --with-sdl --disable-precomp-headers
  make
  make -C locale allmo
  make -C contrib/src
}

package() {
  cd wx*-${pkgver}
  make DESTDIR="${pkgdir}" install
  make -C contrib/src DESTDIR="${pkgdir}" install
  install -D -m644 docs/licence.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
