# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=6
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
source=(https://github.com/michaellass/${pkgname}/archive/v${pkgver}.tar.gz)
sha256sums=('312c7c0dc58e682a4b5246238032c583c0b46f94e459d919069c741156016c48')

package() {
  cd  "${srcdir}/${pkgname}-${pkgver}"
  make PREFIX=/usr DESTDIR="${pkgdir}" install
}
