# Maintainer: Jean-Marc Lenoir <archlinux "at" jihemel "dot" com>
# Contributor: xsmile <sascha_r at gmx dot de>
# Contributor: Denis 'GNUtoo' Carikli <GNUtoo@cyberdimension.org>

pkgname=uefipatch
_tools=('UEFIPatch' 'UEFIReplace')
pkgver=0.28.0
pkgrel=1
pkgdesc='Modifying UEFI firmware images'
arch=('armv7h' 'i686' 'x86_64')
url='https://github.com/LongSoft/UEFITool'
license=('BSD')
depends=('qt5-base')
source=("UEFITool-${pkgver}.tar.gz::https://github.com/LongSoft/UEFITool/archive/${pkgver}.tar.gz")
sha512sums=('5db9b2004dcc8482dd03713fd67b86cabb93455723e1cafad1ec9b877b0b73354e7f692dd3f5ff7ecc5992d6abd5ca2fb5b0cd2d103f4e722320164539d29483')

_build() {
  qmake QMAKE_CFLAGS_RELEASE="$CFLAGS" QMAKE_CXXFLAGS_RELEASE="$CXXFLAGS"
  make
}

build() {
  for tool in "${_tools[@]}"; do
    cd "${srcdir}/UEFITool-${pkgver}/${tool}"
    _build
  done
}

package() {
  cd "${srcdir}/UEFITool-${pkgver}"
  # Install tools
  for tool in "${_tools[@]}"; do
    install -Dm755 "${tool}/${tool}" "${pkgdir}/usr/bin/${tool,,}"
  done
  # Install patches.txt
  install -Dm644 UEFIPatch/patches.txt "${pkgdir}/usr/share/${pkgname}/patches.txt"
  # License
  install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
