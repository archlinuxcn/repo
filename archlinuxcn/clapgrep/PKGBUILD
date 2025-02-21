# Maintainer: Integral <integral@member.fsf.org>

pkgname=clapgrep
pkgver=25.02
pkgrel=1
pkgdesc="One app to search through all your files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/luleyleo/${pkgname}"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'gtksourceview5')
makedepends=('meson' 'cargo' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('a05d3ac660ee9e38e091b9a7af3dad2a80e08dc7fa19a6570d7fc75464c4854b')

build() {
	arch-meson "${pkgname}-${pkgver}/" build
	meson compile -C build
}

check() {
	meson test -C build --print-errorlogs
}

package() {
	meson install -C build --destdir "${pkgdir}"
}
