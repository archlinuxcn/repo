# $Id: PKGBUILD 112889 2014-06-09 12:13:59Z foutrelis $
# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: M0Rf30
# Contributor: Samsagax <samsagax@gmail.com>

pkgname=bbswitch-beignet-fix
pkgver=0.8
_extramodules=extramodules-4.0-beignet-fix # Don't forget to update bbswitch.install
pkgrel=18
pkgdesc="Kernel module allowing to switch dedicated graphics card on Optimus laptops"
arch=('i686' 'x86_64')
url=("http://github.com/Bumblebee-Project/bbswitch")
license=('GPL')
depends=('linux-beignet-fix>=4.0' 'linux-beignet-fix<4.1')
makedepends=('linux-beignet-fix-headers>=4.0' 'linux-beignet-fix-headers<4.1')
install=bbswitch.install
source=("https://github.com/Bumblebee-Project/bbswitch/archive/v${pkgver}.tar.gz")
md5sums=('5b116b31ace3604ddf9d1fc1f4bc5807')

build() {
  cd ${srcdir}/bbswitch-${pkgver}

  _kernver="$(cat /usr/lib/modules/${_extramodules}/version)"

  make KDIR=/lib/modules/${_kernver}/build
}

package() {
  cd ${srcdir}/bbswitch-${pkgver}

  install -Dm644 bbswitch.ko \
    "${pkgdir}"/usr/lib/modules/${_extramodules}/bbswitch.ko
  gzip "${pkgdir}/usr/lib/modules/${_extramodules}/bbswitch.ko"
}
