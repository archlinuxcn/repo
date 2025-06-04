# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>
# Maintainer: Naqua Darazaki <n.darazaki@gmail.com>

pkgname=spedread
_pkgname=Spedread
pkgver=2.5.1
pkgrel=1
pkgdesc="GTK speed reading software: Read like a speedrunner!"
arch=('x86_64' 'aarch64')
url="https://github.com/Darazaki/Spedread"
license=('GPL3')
depends=('libadwaita')
makedepends=('meson' 'vala')
checkdepends=('appstream-glib')
source=("${url}/archive/v${pkgver}.tar.gz")
b2sums=('3dbb3b343941b8567b9edb982b0b8a1eb75cc6852e8a01749b30fff7d0296c001b013a039bd7197fdc0733a812e2ef091ea17c9385011e8700ae7fc805a21f1b')

build() {
  arch-meson "$_pkgname-$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"
}
