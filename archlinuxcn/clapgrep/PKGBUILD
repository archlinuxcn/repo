# Maintainer: Integral <integral@member.fsf.org>

pkgname=clapgrep
pkgver=25.03
pkgrel=2
pkgdesc="One app to search through all your files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/luleyleo/${pkgname}"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'gtksourceview5' 'poppler-glib')
makedepends=('meson' 'cargo' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('15e559c3a3cf250350e64c13a14b3808128880449d12e37b4dd28c21e9796cda')

build() {
	arch-meson "${pkgname}-${pkgver}/" build
	meson compile -C build
}

check() {
	meson test -C build --print-errorlogs
}

package() {
	meson install -C build --no-rebuild --destdir "${pkgdir}"
}
