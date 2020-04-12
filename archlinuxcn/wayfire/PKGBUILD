# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wayfire
pkgver=0.4.0
pkgrel=1
pkgdesc="3D wayland compositor"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(cairo 'wf-config>=0.4' libjpeg libinput wlroots)
makedepends=(meson ninja wayland-protocols glm)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=(482167e3e2633a558f12e4defe473d13c192400dccf864c075d17f57c87c4a21)

build() {
	rm -rf build
	arch-meson "${pkgname}-${pkgver}" build
	ninja -C build
}

check () {
	meson test -C build
}

package() {
	DESTDIR="${pkgdir}/" ninja -C build install
	cd "${pkgname}-${pkgver}"
	install -Dm644 wayfire.desktop "${pkgdir}/usr/share/wayland-sessions/wayfire.desktop"
	install -Dm644 wayfire.ini "${pkgdir}/usr/share/doc/${pkgname}/wayfire.ini"
	install -Dm645 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
