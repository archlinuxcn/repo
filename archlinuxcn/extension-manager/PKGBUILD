# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=extension-manager
pkgver=0.2.3
pkgrel=1
pkgdesc="A native tool for browsing, installing, and managing GNOME Shell Extensions"
arch=('x86_64')
url="https://github.com/mjakeman/extension-manager"
license=('GPL3')
depends=('gtk4>=1:4.6.0' 'libadwaita' 'libsoup3' 'json-glib')
makedepends=('meson' 'blueprint-compiler-git' 'gobject-introspection')
checkdepends=('appstream-glib')
source=($url/archive/v$pkgver.tar.gz)
b2sums=('3bd98f67f419c646a4a7b9d1dee656de305eff5e35124f3765d5d9c82aff7d9e7bbeea912f24c0766c95e0c497b070831ee9922747f200bbcd57470a6adcec7e')

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
