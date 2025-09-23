# Maintainer: Integral <integral@member.fsf.org>

pkgname=clapgrep
pkgver=25.09
pkgrel=1
pkgdesc="One app to search through all your files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/luleyleo/${pkgname}"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'gtksourceview5' 'poppler-glib')
makedepends=('meson' 'cargo' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('d8cf46b4280898eef9c611da87eef8f0a698dc507f44f9627582c0a26ebabf62')

build() {
	arch-meson "${pkgname}-${pkgver/+/-}/" build
	meson compile -C build
}

check() {
	meson test -C build --print-errorlogs
}

package() {
	meson install -C build --no-rebuild --destdir "${pkgdir}"
}
