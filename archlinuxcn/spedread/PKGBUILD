# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>
# Maintainer: Naqua Darazaki <n.darazaki@gmail.com>

# Remove this if building against a libadwaita version earlier than 1.2.0
CONFIG_OPTIONS=-Dadw_1_2=true

pkgname=spedread
_pkgname=Spedread
pkgver=2.4.7
pkgrel=1
pkgdesc="GTK speed reading software: Read like a speedrunner!"
arch=('x86_64' 'aarch64')
url="https://github.com/Darazaki/Spedread"
license=('GPL3')
depends=('libadwaita')
makedepends=('meson' 'vala')
checkdepends=('appstream-glib')
source=("${url}/archive/v${pkgver}.tar.gz")
b2sums=('baba802243957e86149a11476a71e0b185a7ae9589c65d08ab5b3da24e7523f104df33ba7e59a1fd68ee6db5c7cc8299a31f1a20527f92b42ba5f7888332f3cb')

build() {
  arch-meson "$_pkgname-$pkgver" build $CONFIG_OPTIONS
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"
}
