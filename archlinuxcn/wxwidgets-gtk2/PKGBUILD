# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=wxwidgets-gtk2
pkgver=3.2.10
pkgrel=1
arch=(x86_64)
url='https://wxwidgets.org'
license=(custom:wxWindows)
makedepends=(cmake gst-plugins-base glu libnotify qt5-base sdl2 libmspack gtk2)
source=(https://github.com/wxWidgets/wxWidgets/releases/download/v$pkgver/wxWidgets-$pkgver.tar.bz2)
sha256sums=('d66e929569947a4a5920699539089a9bda83a93e5f4917fb313a61f0c344b896')

build() {
  cmake -B build-gtk2 -S wxWidgets-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=None \
    -DwxBUILD_TOOLKIT=gtk2 \
    -DwxUSE_OPENGL=ON \
    -DwxUSE_REGEX=sys\
    -DwxUSE_ZLIB=sys \
    -DwxUSE_EXPAT=sys \
    -DwxUSE_LIBJPEG=sys \
    -DwxUSE_LIBPNG=sys \
    -DwxUSE_LIBTIFF=sys \
    -DwxUSE_LIBLZMA=sys \
    -DwxUSE_LIBMSPACK=ON \
    -DwxUSE_PRIVATE_FONTS=ON
  cmake --build build-gtk2
}

package_wxwidgets-gtk2() {
  pkgdesc='GTK+2 implementation of wxWidgets API for GUI'
  depends=(gtk2 gst-plugins-base-libs libsm wxwidgets-common libnotify libmspack sdl2 libtiff)
  conflicts=(wxgtk wxgtk2)
  provides=(wxgtk wxgtk2 wxwidgets)

  DESTDIR="$pkgdir" cmake --install build-gtk2
  rm -r "$pkgdir"/usr/{include,lib/cmake,lib/libwx_base*,bin/wxrc*,share/locale/*/LC_MESSAGES/wxstd*}
  mv "$pkgdir"/usr/bin/wx-config{,-gtk2} # Conflicts with wx-gtk3

  install -Dm644 wxWidgets-$pkgver/docs/licence.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
