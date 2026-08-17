# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: speps <speps at aur dot archlinux dot org>

pkgname=nomacs
pkgver=3.23.3
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
    libstdc++
    libtiff
    opencv      #libopencv_imgproc.so
    qt6-base
    qt6-svg
    quazip-qt6
    )
makedepends=(
    cmake
    git
    gtest # for tests
    ninja
    python
    qt6-tools
    vulkan-headers
    )
optdepends=(
    'kimageformats: support QOI (Quite OK Image Format)'
    'qt6-imageformats: support additional image formats'
    )
source=("git+https://github.com/nomacs/nomacs.git#tag=${pkgver}")
b2sums=('ef320f1a517a093f66155d5cb860f9828477e7e3dd2ac6abb70fca186e0d0204b4cf742831d5b443d39578b1ebb26906c6590872040690e8654584a67f56bf96')

build() {
  # Disable warning Detected locale "C" with character encoding "ANSI_X3.4-1968", which is not UTF-8.
  export LANG=C.UTF-8
  export LC_ALL=C.UTF-8

  local _flags=(
    -DQT_VERSION_MAJOR=6
    -DENABLE_QUAZIP=ON
    -DENABLE_TRANSLATIONS=ON
    -GNinja
  )

  cmake -B build -S "nomacs/ImageLounge" -Wno-author \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    "${_flags[@]}"

  cmake --build build
}

check() {
  ninja -C build check
}

package() {
  DESTDIR="${pkgdir}" cmake --install build
}
