# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=10
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
source=(https://github.com/michaellass/${pkgname}/archive/v${pkgver}.tar.gz)
sha256sums=('2720310cde4ed064c4387d52d381079479bc8b7390b7cf3333239c4552ae6f80')

package() {
  cd  "${srcdir}/${pkgname}-${pkgver}"
  make PREFIX=/usr DESTDIR="${pkgdir}" install
}
