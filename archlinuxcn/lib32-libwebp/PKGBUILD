# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: carstene1ns <arch.carsten@teibes.de>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Jon Nordby <jononor@gmail.com>

pkgname=lib32-libwebp
pkgver=1.6.0
pkgrel=1
pkgdesc="WebP library (32-bit)"
url="https://developers.google.com/speed/webp/"
arch=(x86_64)
license=(BSD-3-Clause)
depends=(
  lib32-gcc-libs
  lib32-glibc
  libwebp
)
makedepends=(
  cmake
  ninja
)
provides=(
  libsharpyuv.so
  libwebp{,decoder,demux,mux}.so
)
source=(
  https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-$pkgver.tar.gz{,.asc}
)
sha256sums=('e4ab7009bf0629fd11982d4c2aa83964cf244cffba7347ecd39019a9e38c4564'
            'SKIP')
b2sums=('cbdfa8616edce14bf3f8621d9d0d925884d0f40e8775c7d8810575c8bec88f10ed912029cc0a4bccf9bb9eb98824e4b1a89ec61ee53d7ef20a150450d8513168'
        'SKIP')
validpgpkeys=(
  6B0E6B70976DE303EDF2F601F9C3D6BDB8232B5D # WebP release signing key
)

prepare() {
  cd libwebp-$pkgver
}

build() {
  local cmake_options=(
    -D BUILD_SHARED_LIBS=ON
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_LIBDIR=/usr/lib32
    -D CMAKE_INSTALL_PREFIX=/usr
    -D CMAKE_SKIP_INSTALL_RPATH=ON
    -D WEBP_BUILD_CWEBP=OFF
    -D WEBP_BUILD_DWEBP=OFF
    -D WEBP_BUILD_EXTRAS=OFF
    -D WEBP_BUILD_GIF2WEBP=OFF
    -D WEBP_BUILD_IMG2WEBP=OFF
    -D WEBP_BUILD_VWEBP=OFF
  )

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG=i686-pc-linux-gnu-pkg-config

  # Mimic autotools build without --enable-asserts
  CFLAGS+=" -DNDEBUG"
  CXXFLAGS+=" -DNDEBUG"

  cmake -S libwebp-$pkgver -B build -G Ninja "${cmake_options[@]}"
  cmake --build build
}

check() {
  ctest --test-dir build --output-on-failure --stop-on-failure -j$(nproc)
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  rm -r "$pkgdir"/usr/{bin,include,share}

  install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 \
    libwebp-$pkgver/COPYING
}

# vim:set sw=2 sts=-1 et:
