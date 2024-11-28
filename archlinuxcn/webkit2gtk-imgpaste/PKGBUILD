# Maintainer: q234 rty <q23456yuiop at gmail dot com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk-imgpaste
pkgver=2.46.4
pkgrel=1
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
  PasteBoardGtk.patch
)
sha256sums=('0eff5f0ab0a2872ec87df62bc32e3289c8af625716ac71e94b298d74e0374176'
            'SKIP'
            '71b8a59c78d549fed0cd895207f49c7b3be40b236e96f4d7b9907a26521499bf'
            '20ebac2caf15fa546e6da00cb0fa90d5d37fcf7bfa883014d7d15eb4963d12d2')
validpgpkeys=(
  # https://www.webkitgtk.org/verifying.html
  5AA3BC334FD7E3369E7C77B291C559DBE4C9123B # Adrián Pérez de Castro <aperez@igalia.com>
  013A0127AC9C65B34FFA62526C1009B693975393 # Carlos Garcia Campos <cgarcia@igalia.com>
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
    -DUSE_GTK4=OFF
    -DUSE_LIBBACKTRACE=OFF
    -DUSE_SOUP2=ON
    -DENABLE_DOCUMENTATION=ON
    -DENABLE_MINIBROWSER=ON
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
