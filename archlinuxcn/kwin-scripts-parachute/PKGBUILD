# Maintainer: Alejandro Valdes <alejandrovaldes at live dot com>

_pkgname=Parachute
pkgname=kwin-scripts-parachute
pkgver=0.9.1
pkgrel=1
pkgdesc="Windows and desktops from above"
arch=(any)
url="https://github.com/tcorreabr/${_pkgname}"
license=(GPLv3)
depends=(kwin)
makedepends=(kpackage)
source=("$url/archive/v${pkgver}.zip")
sha256sums=('ca09a6b569d275063d98448f556e58e2ffae0302e16df72ebbdc586c2badd326')

package() {
  cd $srcdir/${_pkgname}-${pkgver}/
  kpackagetool5 --type Kwin/Script --install . -p "${pkgdir}/usr/share/kwin/scripts/"
  install -Dm644 metadata.desktop "${pkgdir}/usr/share/kservices5/${_pkgname}.desktop"
}
