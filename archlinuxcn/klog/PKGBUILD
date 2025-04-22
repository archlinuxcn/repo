# Maintainer:  Andrew O'Neill <andrew at haunted dot sh>
# Contributor: Gavin Lloyd <gavinhungry@gmail.com>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

pkgname=klog
pkgver=2.4.0
pkgrel=1
pkgdesc='A multiplatform free hamradio logger'
arch=('x86_64')
url="https://github.com/ea4k/${pkgname}"
license=('GPL-3.0-only')
makedepends=('qt6-tools' 'gendesk')
depends=('qt6-base' 'qt6-charts' 'qt6-declarative' 'qt6-location' 'qt6-serialport' 'hamlib')
options=('!makeflags')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('16f45a60cc18b444a602ad0d970372b8b842486a4506da67bf1cea059cd7241c')

prepare() {
  cd "${pkgname}-${pkgver}"

  gendesk --pkgname "${pkgname}" --pkgdesc "${pkgdesc}" --exec "/usr/bin/${pkgname}" -n
}

build() {
  cd "${pkgname}-${pkgver}"

  qmake6 PREFIX=/usr KLog.pro
  make
}

package() {
  cd "${pkgname}-${pkgver}"

  install -Dm755 src/build/target/klog "${pkgdir}/usr/bin/klog"
  install -Dm644 src/klog.1 "${pkgdir}/usr/share/man/man1/klog.1"
  install -Dm644 src/img/${pkgname}_512x512.png "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install -Dm644 ${pkgname}.desktop "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
