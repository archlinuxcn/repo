# $Id: PKGBUILD 294869 2017-04-27 03:06:45Z foutrelis $
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=webkitgtk
pkgname=(webkitgtk webkitgtk2)
pkgver=2.4.11
pkgrel=6
pkgdesc="Legacy Web content engine"
arch=(i686 x86_64)
url="https://webkitgtk.org/"
license=(custom)
depends=(libxt libxslt sqlite libsoup enchant libgl geoclue2 gst-plugins-base-libs
         libsecret libwebp harfbuzz-icu)
makedepends=(gtk3 gtk2 gperf gobject-introspection python2 mesa ruby)
optdepends=('gst-plugins-base: free media decoding'
            'gst-plugins-good: media decoding'
            'gst-libav: nonfree media decoding')
options=(!emptydirs)
install=webkitgtk.install
source=(https://webkitgtk.org/releases/$pkgbase-${pkgver}.tar.xz
        webkitgtk-2.4.9-abs.patch
        icu59.patch)
sha256sums=('588aea051bfbacced27fdfe0335a957dca839ebe36aa548df39c7bbafdb65bf7'
            'ec294bbb5588a1802a68e3615c6718486b22f922645c5fef686d3d103014bf70'
            'eb791b9c8dcb84996904846dedf8c3ddf1a5fde32330177f3f0071510bd8ca6d')

prepare() {
  mkdir build-gtk{,2} path
  ln -s /usr/bin/python2 path/python

  cd $pkgbase-$pkgver
  patch -Np1 -i ../webkitgtk-2.4.9-abs.patch
  patch -Np1 -i ../icu59.patch
}

_build() (
  _ver="$1"; shift
  cd build-${_ver}

  PATH="$srcdir/path:$PATH"

  CXXFLAGS+=" -fno-delete-null-pointer-checks"
  CFLAGS+=" -fno-delete-null-pointer-checks"

  ../$pkgbase-$pkgver/configure --prefix=/usr \
    --libexecdir=/usr/lib/webkit${_ver} \
    --enable-introspection \
    --disable-webkit2 \
    --disable-gtk-doc \
    "$@"

  # https://bugzilla.gnome.org/show_bug.cgi?id=655517
  sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make all stamp-po
)

build() {
  _build gtk
  _build gtk2 --with-gtk=2.0
}

package_webkitgtk() {
  pkgdesc+=" for GTK+ 3"
  depends+=(gtk3)
  optdepends+=('gtk2: Netscape plugin support')
  provides=("webkitgtk3=${pkgver}" "libwebkit3=${pkgver}")
  conflicts=(webkitgtk3 libwebkit3)
  replaces=(webkitgtk3 libwebkit3)

  make -C build-gtk -j1 DESTDIR="$pkgdir" install
  install -Dm644 $pkgbase-$pkgver/Source/WebKit/LICENSE \
    "$pkgdir/usr/share/licenses/webkitgtk/LICENSE"
}

package_webkitgtk2() {
  pkgdesc+=" for GTK+ 2"
  depends+=(gtk2)
  provides=("libwebkit=${pkgver}")
  conflicts=(libwebkit)
  replaces=(libwebkit)

  make -C build-gtk2 -j1 DESTDIR="$pkgdir" install
  install -Dm644 $pkgbase-$pkgver/Source/WebKit/LICENSE \
    "$pkgdir/usr/share/licenses/webkitgtk2/LICENSE"
}
