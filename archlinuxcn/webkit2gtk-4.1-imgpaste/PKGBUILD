# Maintainer: q234 rty <q23456yuiop at gmail dot com>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk-4.1-imgpaste
pkgver=2.42.5
pkgrel=1
pkgdesc="Web content engine for GTK (with patches for pasting images from clipboard)"
url="https://webkitgtk.org"
arch=(x86_64)
license=('LicenseRef-custom')
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
  libjpeg
  libjxl
  libmanette
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
  clang
  cmake
  gi-docgen
  gobject-introspection
  gperf
  gst-plugins-bad
  lld
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
  GTK-MiniBrowser-should-hide-the-toolbar-when-using-full-screen.patch
  GTK-Disable-DMABuf-renderer-for-NVIDIA-proprietary-drivers.patch
)
sha256sums=('b64278c1f20b8cfdbfb5ff573c37d871aba74a1db26d9b39f74e8953fe61e749'
            'SKIP'
            '71b8a59c78d549fed0cd895207f49c7b3be40b236e96f4d7b9907a26521499bf'
            '20ebac2caf15fa546e6da00cb0fa90d5d37fcf7bfa883014d7d15eb4963d12d2'
            'a921d6be1303e9f23474971f381886fd291ec5bb1a7ff1e85acede8cfb88bef2'
            '655f3b2c96355ac83c4fa1fc6048e3256bbfdbfb9727e1e18c5af12613536206')
validpgpkeys=(
  'D7FCF61CF9A2DEAB31D81BD3F3D322D0EC4582C3'  # Carlos Garcia Campos <cgarcia@igalia.com>
  '5AA3BC334FD7E3369E7C77B291C559DBE4C9123B'  # Adrián Pérez de Castro <aperez@igalia.com>
)

prepare() {
  cd webkitgtk-$pkgver

  patch -Np1 -i ../PasteBoardGtk.patch
  patch -Np1 -i ../EnlargeObjectSize.patch
  # Requested by eworm
  # https://github.com/WebKit/WebKit/pull/17909
  patch -Np1 -i ../GTK-MiniBrowser-should-hide-the-toolbar-when-using-full-screen.patch

  # https://bugs.archlinux.org/task/79783
  # https://github.com/WebKit/WebKit/pull/18614
  patch -Np1 -i ../GTK-Disable-DMABuf-renderer-for-NVIDIA-proprietary-drivers.patch
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

  # GCC with LTO fails to link libjavascriptcoregtk
  #     /usr/bin/ld: /tmp/ccXxyWZV.ltrans0.ltrans.o: in function `ipint_table_size_validate':
  #     <artificial>:(.text+0x49f0f): undefined reference to `ipint_extern_table_size'
  #     /usr/bin/ld: /tmp/ccXxyWZV.ltrans0.ltrans.o: in function `ipint_table_fill_validate':
  #     <artificial>:(.text+0x4a019): undefined reference to `ipint_extern_table_fill'
  #     collect2: error: ld returned 1 exit status
  export CC=clang CXX=clang++
  LDFLAGS+=" -fuse-ld=lld"

    # JITted code crashes when CET is used
  CFLAGS+=' -fcf-protection=none'
  CXXFLAGS+=' -fcf-protection=none'

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
