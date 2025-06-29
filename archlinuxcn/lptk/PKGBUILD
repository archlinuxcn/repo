# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)

pkgname=lptk
pkgver=0.6.0
pkgrel=1
pkgdesc='Stateless password manager'
arch=('aarch64' 'x86_64')
url='https://gitlab.com/ogarcia/lptk'
license=('GPL-3.0-or-later')
depends=('libadwaita' 'gtksourceview5')
makedepends=('git' 'meson' 'rust')
source=("${pkgname}::git+https://gitlab.com/ogarcia/${pkgname}.git#tag=${pkgver}")
b2sums=('696957a739a028659b325664dfd3c6081e020aae7a180b34362986781f27071f64fd9cf154f5fd8606d51e97d30696492df22409410130c52d8fbecbcc7f3db0')

build() {
  arch-meson "${pkgname}" build
  meson compile -C build
}

package() {
  meson install -C build --destdir "${pkgdir}"
}
