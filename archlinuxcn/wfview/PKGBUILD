# Maintainer: envolution
# Contributor: FuzzyCheese
# shellcheck shell=bash disable=SC2034,SC2154
pkgname=wfview
pkgver=2.25
pkgrel=1
pkgdesc="Interface for Icom transceivers"
arch=('i686' 'x86_64')
url="https://wfview.org/"
license=('GPL-3.0-only')
depends=(
  qt5-serialport 
  qt5-multimedia 
  qcustomplot 
  eigen 
  qt5-gamepad 
  rtaudio 
  qt5-websockets 
  opus 
  hidapi 
  portaudio
  glibc
  qt5-base
  systemd-libs
  gcc-libs
)

source=("$pkgname-$pkgver.tar.gz::https://github.com/wf-group/wfview/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('e3db5ccd2f8e2c4dab16604d6c63d903bb5cc770620916fa84260822489a4766')

prepare() {
  cd "$pkgname-$pkgver"
  echo "linux:LIBS += -lqcustomplot" >>wfview.pro
}

build() {
  cd "${pkgname}-${pkgver}"
  mkdir -p build
  cd build
  qmake ../wfview.pro PREFIX=/usr VERSION="$pkgver"
  make
}

package() {
  cd "${pkgname}-${pkgver}/build"
  make INSTALL_ROOT="${pkgdir}" install
}
# vim:set ts=2 sw=2 et:
