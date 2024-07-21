# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=cartridges
pkgver=2.9.3
pkgrel=1
pkgdesc="A GTK4 + Libadwaita game launcher"
arch=(any)
url="https://github.com/kra-mo/cartridges"
license=(GPL3)
depends=(gtk4 libadwaita gdk-pixbuf2 gobject-introspection-runtime python python-gobject python-requests python-yaml
         python-pillow python-urllib3 dconf hicolor-icon-theme)
makedepends=(blueprint-compiler meson)
checkdepends=(appstream-glib)
optdepends=("steam: Valve's digital software delivery system"
            'heroic-games-launcher: Native GOG and Epic Games launcher for Linux'
            'bottles: Easily manage wine and proton prefix')
source=(${pkgname}-${pkgver}.tar.gz::$url/archive/v${pkgver}.tar.gz)
b2sums=('0e9700e7ab78b303e6f8a50654053233f72a4e684cbee529af252a027ade1dd7d9496c6d7539c177959fd55628b9b35d785daa1152f192edf2f477e11f08d0bf')

build() {
  arch-meson "${pkgname}-${pkgver}" build  -D tiff_compression=jpeg
  meson compile -C build
}

check() {
  # https://github.com/kra-mo/cartridges/issues/206
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"
}
