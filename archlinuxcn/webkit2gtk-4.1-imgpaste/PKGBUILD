# Maintainer: q234 rty <q23456yuiop at gmail dot com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk-4.1-imgpaste
pkgver=2.38.5
pkgrel=1
pkgdesc="Web content engine for GTK (with patches for pasting images from clipboard)"
url="https://webkitgtk.org"
arch=(x86_64)
license=(custom)
depends=(
  at-spi2-core
  atk
  bubblewrap
  cairo
  enchant
  fontconfig
  freetype2
  glib2
  gst-plugins-base-libs
  gstreamer
  gtk3
  harfbuzz
  harfbuzz-icu
  hyphen
  icu
  libavif
  libegl
  libgcrypt
  libgl
  libgles
  libice
  libjpeg
  libmanette
  libnotify
  libpng
  libseccomp
  libsecret
  libsoup3
  libsystemd
  libtasn1
  libwebp
  libwpe
  libx11
  libxext
  libxml2
  libxslt
  libxt
  openjpeg2
  sqlite
  wayland
  woff2
  wpebackend-fdo
  xdg-dbus-proxy
  zlib
)
makedepends=(
  cmake
  gi-docgen
  gobject-introspection
  gperf
  gst-plugins-bad
  ninja
  python
  ruby
  systemd
  wayland-protocols
)
provides=(webkit2gtk-4.1)
conflicts=(webkit2gtk-4.1)
source=($url/releases/webkitgtk-$pkgver.tar.xz{,.asc}
        EnlargeObjectSize.patch
        PasteBoardGtk.patch)
sha256sums=('40c20c43022274df5893f22b1054fa894c3eea057389bb08aee08c5b0bb0c1a7'
            'SKIP'
            'a5d2149d55190a15bc806bfddd85f43b6c714722b04ce0c1e476f9cb58985bac'
            '909eb44783d093c89400494a8b57eee3a5b926e1a5b5f1e922e1dff1a6dc3c7b')
validpgpkeys=('D7FCF61CF9A2DEAB31D81BD3F3D322D0EC4582C3'  # Carlos Garcia Campos <cgarcia@igalia.com>
              '5AA3BC334FD7E3369E7C77B291C559DBE4C9123B') # Adrián Pérez de Castro <aperez@igalia.com>

prepare() {
  cd webkitgtk-$pkgver
  patch -Np0 -i ../PasteBoardGtk.patch
  patch -Np0 -i ../EnlargeObjectSize.patch
}

build() {
  # Produce minimal debug info: 4.3 GB of debug data makes the
  # build too slow and is too much to package for debuginfod
  CFLAGS+=' -g1'
  CXXFLAGS+=' -g1'
  
  cmake -S webkitgtk-$pkgver -B build -G Ninja \
    -DPORT=GTK \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DCMAKE_SKIP_RPATH=ON \
    -DUSE_AVIF=ON \
    -DUSE_SOUP2=OFF \
    -DENABLE_DOCUMENTATION=ON \
    -DENABLE_MINIBROWSER=ON
  cmake --build build
}

package() {
  depends+=(libwpe-1.0.so libWPEBackend-fdo-1.0.so)
  provides+=(libjavascriptcoregtk-4.1.so libwebkit2gtk-4.1.so)
  optdepends=('geoclue: Geolocation support'
              'gst-plugins-good: media decoding'
              'gst-plugins-bad: media decoding'
              'gst-libav: nonfree media decoding')

  DESTDIR="$pkgdir" cmake --install build

  rm -r "$pkgdir/usr/bin"

  mkdir -p doc/usr/share
  mv {"$pkgdir",doc}/usr/share/gtk-doc

  cd webkitgtk-$pkgver
  find Source -name 'COPYING*' -or -name 'LICENSE*' -print0 | sort -z |
    while IFS= read -d $'\0' -r _f; do
      echo "### $_f ###"
      cat "$_f"
      echo
    done |
    install -Dm644 /dev/stdin "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set sw=2 sts=-1 et:
