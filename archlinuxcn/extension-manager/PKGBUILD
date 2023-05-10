# Maintainer: Igor Dyatlov <dyatlov.igor@protonmail.com>

pkgname=extension-manager
pkgver=0.4.1
pkgrel=1
pkgdesc="A native tool for browsing, installing, and managing GNOME Shell Extensions"
arch=('x86_64' 'aarch64')
url="https://github.com/mjakeman/extension-manager"
license=('GPL3')
depends=('libadwaita' 'libsoup3' 'json-glib' 'text-engine' 'libbacktrace-git')
makedepends=('meson' 'blueprint-compiler' 'gobject-introspection')
checkdepends=('appstream-glib')
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
b2sums=('ca7c4dabc100d4a8aba8a41ecdec3c88676764b81c2e5fdb64785ca5031a31749d058c1a670867fd1028ae13721d8de0c648fd397f63a56871e11899bca4d4f5')

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
