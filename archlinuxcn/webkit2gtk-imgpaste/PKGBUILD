# Maintainer: q234 rty <q23456yuiop at gmail dot com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk-imgpaste
pkgver=2.50.1
pkgrel=2
pkgdesc="Web content engine for GTK (with patches for pasting images from clipboard)"
url="https://webkitgtk.org"
arch=(x86_64)
license=(
  # :sort ui /\v^\s*['"]?/
  'AFL-2.0 OR GPL-2.0-or-later'
  Apache-2.0
  'Apache-2.0 WITH LLVM-exception'
  BSD-2-Clause
  BSD-2-Clause-Views
  BSD-3-Clause
  BSD-Source-Code
  BSL-1.0
  bzip2-1.0.6
  GPL-2.0-only
  'GPL-3.0-only WITH Autoconf-exception-3.0'
  'GPL-3.0-or-later WITH Bison-exception-2.2'
  ICU
  ISC
  LGPL-2.1-only
  LGPL-2.1-or-later
  MIT
  MPL-1.1
  MPL-2.0
  NCSA
  'NCSA OR MIT'
  OFL-1.1
  SunPro
  Unicode-TOU
)
depends=(
  at-spi2-core
  atk
  bubblewrap
  cairo
  enchant
  fontconfig
  freetype2
  gcc-libs
  gdk-pixbuf2
  glib2
  glibc
  gst-plugins-bad-libs
  gst-plugins-base-libs
  gstreamer
  gtk3
  harfbuzz
  harfbuzz-icu
  hyphen
  icu
  lcms2
  libavif
  libdrm
  libegl
  libepoxy
  libgcrypt
  libgl
  libgles
  libjpeg-turbo
  libjxl
  libmanette
  libpng
  libseccomp
  libsecret
  libsoup
  libsystemd
  libtasn1
  libwebp
  libx11
  libxml2
  libxslt
  mesa
  openjpeg2
  pango
  sqlite
  ttf-font
  wayland
  woff2
  xdg-dbus-proxy
  zlib
)
makedepends=(
  clang
  cmake
  gi-docgen
  glib2-devel
  gobject-introspection
  gperf
  gst-plugins-bad
  lld
  ninja
  python
  ruby
  ruby-stdlib
  systemd
  unifdef
  wayland-protocols
)
provides=(webkit2gtk)
conflicts=(webkit2gtk)
source=(
  $url/releases/webkitgtk-$pkgver.tar.xz{,.asc}
  EnlargeObjectSize.patch
  PasteBoardGLib.patch
)
sha256sums=('33e912ee6e3cdb4b9803715f50686af85a60af47f1cf72a6acc6a2db1bb3d9fe'
            'SKIP'
            '71b8a59c78d549fed0cd895207f49c7b3be40b236e96f4d7b9907a26521499bf'
            'a6b7fd668a42dc27cd6ea0fec5eb3501ab8241e18b4bd6c8844ad6bd3207cf6e')
validpgpkeys=(
  # https://www.webkitgtk.org/verifying.html
  5AA3BC334FD7E3369E7C77B291C559DBE4C9123B # Adrián Pérez de Castro <aperez@igalia.com>
  013A0127AC9C65B34FFA62526C1009B693975393 # Carlos Garcia Campos <cgarcia@igalia.com>
)

prepare() {
  cd webkitgtk-$pkgver

  patch -Np1 -i ../PasteBoardGLib.patch
  patch -Np1 -i ../EnlargeObjectSize.patch
}

build() {
  local cmake_options=(
    -D CMAKE_BUILD_TYPE=Release
    -D CMAKE_INSTALL_LIBDIR=lib
    -D CMAKE_INSTALL_LIBEXECDIR=lib
    -D CMAKE_INSTALL_PREFIX=/usr
    -D CMAKE_SKIP_RPATH=ON
    -D ENABLE_DOCUMENTATION=ON
    -D ENABLE_MINIBROWSER=ON
    -D ENABLE_SPEECH_SYNTHESIS=OFF
    -D PORT=GTK
    -D USE_FLITE=OFF
    -D USE_GTK4=OFF
    -D USE_LIBBACKTRACE=OFF
    -D USE_SOUP2=ON
  )

  # Upstream prefers Clang
  # https://gitlab.archlinux.org/archlinux/packaging/packages/webkitgtk-6.0/-/issues/4
  export CC=clang CXX=clang++
  LDFLAGS+=" -fuse-ld=lld"

  # Skia uses malloc_usable_size
  CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"

  # JITted code crashes when CET is used
  CFLAGS+=' -fcf-protection=none'
  CXXFLAGS+=' -fcf-protection=none'

  cmake -S webkitgtk-$pkgver -B build -G Ninja "${cmake_options[@]}"
  cmake --build build
}

package() {
  provides+=(
    libjavascriptcoregtk-4.0.so
    libwebkit2gtk-4.0.so
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
  mv {"$pkgdir",doc}/usr/share/doc

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
