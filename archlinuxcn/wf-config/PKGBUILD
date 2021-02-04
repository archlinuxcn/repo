# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wf-config
pkgver=0.7.0
pkgrel=1
pkgdesc="A library for managing configuration files, written for wayfire"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(libevdev libxml2)
makedepends=(meson ninja pkg-config wayland-protocols glm)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=(c7fb0b388afdd46add4b209ff7262bd3a30f9948a9a4d6e7ec1239bbf42b5aad)

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
