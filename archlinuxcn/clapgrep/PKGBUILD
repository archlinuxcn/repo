# Maintainer: Integral <integral@member.fsf.org>

pkgname=clapgrep
pkgver=25.10
pkgrel=1
pkgdesc="One app to search through all your files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/luleyleo/${pkgname}"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'gtksourceview5' 'poppler-glib')
makedepends=('meson' 'cargo' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('b1048a9d1441238ef679bb8142ba98187eb1e135560a52780d00e388745f51e4')

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
