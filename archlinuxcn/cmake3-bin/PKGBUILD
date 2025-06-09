# Maintainer: Franck Duriez <franck dot lucien dot duriez at gmail dot com>

_pkgname=cmake3
pkgname=${_pkgname}-bin
pkgver=3.31.6
pkgrel=1
pkgdesc="A cross-platform open-source make system"
arch=('x86_64' 'aarch64')
url='https://cmake.org'
license=('custom')
options=('!strip' 'staticlibs')
provides=("${_pkgname}")
conflicts=("${_pkgname}")

source_x86_64=("${pkgname}-${pkgver}-x86_64.tar.gz"::"https://github.com/Kitware/CMake/releases/download/v${pkgver}/cmake-${pkgver}-linux-x86_64.tar.gz")
source_aarch64=("${pkgname}-${pkgver}-aarch64.tar.gz"::"https://github.com/Kitware/CMake/releases/download/v${pkgver}/cmake-${pkgver}-linux-aarch64.tar.gz")

package() {
  install -d "$pkgdir/opt/cmake3"
  install -d "$pkgdir/usr/bin"
  cp -ar "${srcdir}/cmake-${pkgver}-linux-${CARCH}/"* "${pkgdir}/opt/cmake3"
  for PROG in ccmake cmake cmake-gui cpack ctest; do
    ln -s "/opt/cmake3/bin/$PROG" "${pkgdir}/usr/bin/${PROG}3"
  done
}

md5sums_x86_64=('8514fe0197f534eef079097c774c221a')
md5sums_aarch64=('62ce31eb181907572382268134a8f1c7')

