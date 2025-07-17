# Maintainer: envolution
# Contributor: FuzzyCheese
# shellcheck shell=bash disable=SC2034,SC2154
pkgname=wfview
pkgver=2.11
pkgrel=2
pkgdesc="Interface for Icom transceivers"
arch=('i686' 'x86_64')
url="https://wfview.org/"
license=('GPL-3.0-only')
depends=('qt5-serialport' 'qt5-multimedia' 'qcustomplot' 'eigen' 'qt5-gamepad' 'rtaudio' 'qt5-websockets' 'opus' 'hidapi' 'portaudio')

provides=('wfview')
source=("https://gitlab.com/eliggett/wfview/-/archive/v$pkgver/wfview-v$pkgver.tar.gz")
md5sums=('cbd4c4fec0a6bf922ccdc71e4a2ebe88')

prepare() {
  sed -i '/^linux:QMAKE_POST_LINK += echo; echo; echo "Run install.sh as root from the build directory to install."; echo; echo;$/s/^/#/' ${srcdir}/wfview-v$pkgver/wfview.pro
  echo "linux:LIBS += -lqcustomplot" >> ${srcdir}/wfview-v$pkgver/wfview.pro
}

build() {
  cd "${srcdir}"
  mv wfview-v$pkgver wfview
  mkdir -p build
  cd build
  qmake ../wfview/wfview.pro PREFIX=/usr
  make
}

package() {
  install -D "${srcdir}/build/wfview" "$pkgdir/usr/bin/wfview"
  install -D "${srcdir}/wfview/resources/wfview.desktop" "$pkgdir/usr/share/applications/wfview.desktop"
  install -D "${srcdir}/wfview/resources/wfview.png" "$pkgdir/usr/share/pixmaps/wfview.png"
  mkdir -p "$pkgdir/usr/share/wfview/stylesheets/qdarkstyle"
  cp -rv "${srcdir}/wfview/qdarkstyle" -t "$pkgdir/usr/share/wfview/stylesheets"
}
# vim:set ts=2 sw=2 et:
