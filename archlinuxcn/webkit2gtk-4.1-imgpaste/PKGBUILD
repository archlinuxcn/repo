# Maintainer: q234 rty <q23456yuiop at gmail dot com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk-4.1-imgpaste
pkgver=2.40.1
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
  gst-plugins-bad-libs
  gst-plugins-base-libs
  gstreamer
  gtk3
  harfbuzz
  harfbuzz-icu
  hyphen
  icu
  libavif
  libdrm
  libegl
  libepoxy
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
  libxcomposite
  libxext
  libxml2
  libxslt
  libxt
  mesa
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
  unifdef
  wayland-protocols
)
provides=(webkit2gtk-4.1)
conflicts=(webkit2gtk-4.1)
source=(
  $url/releases/webkitgtk-$pkgver.tar.xz{,.asc}
  EnlargeObjectSize.patch
  PasteBoardGtk.patch
)
sha256sums=('64e526984f8cd2161ef03ae949af99c002ff333d615e6386b460164a3c1b7ef6'
            'SKIP'
            '71b8a59c78d549fed0cd895207f49c7b3be40b236e96f4d7b9907a26521499bf'
            '20ebac2caf15fa546e6da00cb0fa90d5d37fcf7bfa883014d7d15eb4963d12d2')
validpgpkeys=(
  'D7FCF61CF9A2DEAB31D81BD3F3D322D0EC4582C3'  # Carlos Garcia Campos <cgarcia@igalia.com>
  '5AA3BC334FD7E3369E7C77B291C559DBE4C9123B'  # Adrián Pérez de Castro <aperez@igalia.com>
)

prepare() {
  cd webkitgtk-$pkgver
  patch -Np1 -i ../PasteBoardGtk.patch
  patch -Np1 -i ../EnlargeObjectSize.patch
}

build() {
  local cmake_options=(
    -DPORT=GTK
    -DCMAKE_BUILD_TYPE=Release
    -DCMAKE_INSTALL_PREFIX=/usr
    -DCMAKE_INSTALL_LIBDIR=lib
    -DCMAKE_INSTALL_LIBEXECDIR=lib
    -DCMAKE_SKIP_RPATH=ON
    -DUSE_AVIF=ON
    -DUSE_SOUP2=OFF
    -DENABLE_DOCUMENTATION=ON
    -DENABLE_MINIBROWSER=ON
  )

  # Produce minimal debug info: 4.3 GB of debug data makes the
  # build too slow and is too much to package for debuginfod
  CFLAGS+=' -g1'
  CXXFLAGS+=' -g1'

  cmake -S webkitgtk-$pkgver -B build -G Ninja "${cmake_options[@]}"
  cmake --build build
}

package() {
  depends+=(
    libWPEBackend-fdo-1.0.so
    libwpe-1.0.so
  )
  provides+=(
    libjavascriptcoregtk-4.1.so
    libwebkit2gtk-4.1.so
  )
  optdepends=(
    'geoclue: Geolocation support'
    'gst-libav: nonfree media decoding'
    'gst-plugins-bad: media decoding'
    'gst-plugins-good: media decoding'
  )

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
