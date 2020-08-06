# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wf-config
pkgver=0.5.0
pkgrel=1
pkgdesc="A library for managing configuration files, written for wayfire"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(libevdev libxml2)
makedepends=(meson ninja pkg-config wayland-protocols glm)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=(a77c7ec272261b4e49ba605cc5185ad240af277e4124a62c90d5d01b86777b75)

build() {
	rm -rf build
	arch-meson "${pkgname}-${pkgver}" build
	ninja -C build
}

check () {
	meson test -C build
}

package() {
	DESTDIR="${pkgdir}" ninja -C build install
	install -Dm644 "${pkgname}-${pkgver}/LICENSE" \
		"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
