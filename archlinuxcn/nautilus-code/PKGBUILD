# Maintainer: Mazhar Hussain <realmazharhussain@gmail.com>
pkgname=nautilus-code
pkgver=0.5
pkgrel=1
pkgdesc="Adds right-click menu items to open current folder in code editors"
arch=(any)
url="https://github.com/realmazharhussain/nautilus-code"
license=('AGPL3')
depends=('libnautilus-extension')
makedepends=('git' 'meson')
optdepends=("code: for 'Open in VSCode' menu item"
            "gnome-builder: for 'Open in Builder' menu item")
backup=()
source=("${pkgname}-${pkgver}.tar.gz"::"$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('b395a29e412ee873a6a3108b4257837efc4cb8f2584a4f808cc9b720543e5065')

prepare() {
  cd "$srcdir/$pkgname-${pkgver}"
}
build() {
   arch-meson --buildtype=release "${srcdir}/${pkgname}-${pkgver}" build
}
check() {
  meson test -C build --print-errorlogs
}
package() {
  meson install -C build --destdir="$pkgdir"
}
