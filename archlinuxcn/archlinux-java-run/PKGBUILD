# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=8
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
source=(https://github.com/michaellass/${pkgname}/archive/v${pkgver}.tar.gz)
sha256sums=('403242dabc1b4994dc5d39719529f4c13118e2622ac47937cd2f80805f6b914b')

package() {
  cd  "${srcdir}/${pkgname}-${pkgver}"
  make PREFIX=/usr DESTDIR="${pkgdir}" install
}
