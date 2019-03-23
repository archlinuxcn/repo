# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=5
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
source=(https://github.com/michaellass/${pkgname}/archive/v${pkgver}.tar.gz)
sha256sums=('eae4381967bfabbff4705e8b7e42627d9d2e3f667d20af09c9938bf92d9db5c2')

package() {
  cd  "${srcdir}/${pkgname}-${pkgver}"
  make PREFIX=/usr DESTDIR="${pkgdir}" install
}
