# Maintainer: Michael Lass <bevan@bi-co.net>

# This PKGBUILD is maintained on github:
# https://github.com/michaellass/AUR

pkgname=archlinux-java-run
pkgver=4
pkgrel=1
pkgdesc="Java Application Launcher for Arch Linux"
arch=(any)
url="https://github.com/michaellass/archlinux-java-run"
license=('MIT')
depends=(bash java-runtime-common)
makedepends=(git)
source=("archlinux-java-run::git+https://github.com/michaellass/archlinux-java-run.git#tag=v${pkgver}")
sha256sums=('SKIP')

package() {
  cd  "${srcdir}/${pkgname}"
  install -Dm755 archlinux-java-run.sh "${pkgdir}"/usr/bin/archlinux-java-run
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
  install -Dm644 README.md "${pkgdir}"/usr/share/doc/${pkgname}/README.md
}
