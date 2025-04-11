# Maintainer: Integral <integral@member.fsf.org>

pkgname=clapgrep
pkgver=25.04
pkgrel=1
pkgdesc="One app to search through all your files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/luleyleo/${pkgname}"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'gtksourceview5' 'poppler-glib')
makedepends=('meson' 'cargo' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('0cd5bbbab4214d9dc2dabb245bbd88e5d9bc7fb9f6cb9364520fe167cdfbb773')

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
