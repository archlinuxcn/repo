# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: speps <speps at aur dot archlinux dot org>

pkgname=nomacs
pkgver=3.23.2
pkgrel=1
epoch=1
pkgdesc="A Qt image viewer"
arch=(x86_64)
url="https://github.com/nomacs/nomacs"
license=(GPL-3.0-only)
depends=(
    exiv2
    glibc
    hicolor-icon-theme
    libgcc
    libglvnd
    libraw
    libtiff
    opencv      #libopencv_imgproc.so
    qt6-base
    qt6-svg
    quazip-qt6
    )
makedepends=(
    cmake
    git
    #gtest # for tests
    python
    qt6-tools
    vulkan-headers
    )
optdepends=(
    'kimageformats: support QOI (Quite OK Image Format)'
    'qt6-imageformats: support additional image formats'
    )
source=("git+https://github.com/nomacs/nomacs.git#tag=${pkgver}")
b2sums=('ccfd20c66feea7411ad78623f0966d74d94f0012a96186e36616fbea3ff45505bf35459eed50d64be5e40b038acfae6c634a545133c62d4a92e12d33bc53e552')

build() {
  # Disable warning Detected locale "C" with character encoding "ANSI_X3.4-1968", which is not UTF-8.
  export LANG=C.UTF-8
  export LC_ALL=C.UTF-8

  local _flags=(
    -DQT_VERSION_MAJOR=6
    -DUSE_SYSTEM_QUAZIP=ON
    -DENABLE_TRANSLATIONS=ON
  )

  cmake -B build -S "nomacs/ImageLounge" -Wno-author \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    "${_flags[@]}"

  cmake --build build
}

#check() {
  #ctest --test-dir build --output-on-failure
  # tests not built despite nomacs "tests ................................................. YES" ?
#}

package() {
  DESTDIR="${pkgdir}" cmake --install build
}
