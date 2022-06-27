# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=extension-manager
pkgver=0.3.1
pkgrel=1
pkgdesc="A native tool for browsing, installing, and managing GNOME Shell Extensions"
arch=('x86_64' 'aarch64')
url="https://github.com/mjakeman/extension-manager"
license=('GPL3')
depends=('libadwaita' 'libsoup3' 'json-glib' 'text-engine')
makedepends=('meson' 'blueprint-compiler' 'gobject-introspection')
checkdepends=('appstream-glib')
source=($url/archive/v$pkgver.tar.gz)
b2sums=('bd1f6ac1a30521d7ff209c556bcc4ce0103666b9740aa982f0e1a7727b40106df482b693ece920a7449a634955984fa363e217a6b7d14fa0861effe27490824c')

build() {
  arch-meson "${pkgname%-git}-$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build
}

package() {
  meson install -C build --destdir "$pkgdir"
}
