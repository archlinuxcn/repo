# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=extension-manager
pkgver=0.4.0
pkgrel=2
pkgdesc="A native tool for browsing, installing, and managing GNOME Shell Extensions"
arch=('x86_64' 'aarch64')
url="https://github.com/mjakeman/extension-manager"
license=('GPL3')
depends=('libadwaita' 'libsoup3' 'json-glib' 'text-engine' 'libbacktrace-git')
makedepends=('meson' 'blueprint-compiler' 'gobject-introspection' 'python-gobject')
checkdepends=('appstream-glib')
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
b2sums=('9cf6ed74d30e22de8621ff9481de65295d9be07b82134b861192dfe3a9ebad4ea09be136beda0badc78d45cfd15a889b39b907ef4e258bc4229f6a342adde73d')

build() {
  arch-meson $pkgname-$pkgver build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"
}
