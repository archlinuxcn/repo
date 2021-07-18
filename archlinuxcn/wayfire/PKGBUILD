# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wayfire
pkgver=0.7.2
pkgrel=1
pkgdesc="3D wayland compositor"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(cairo 'wf-config>=0.5' libjpeg libinput 'wlroots>=0.14' 'wlroots<0.15')
makedepends=(meson ninja wayland-protocols glm cmake doctest)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=(c6785613df438e64aa5dcce798a0205c83cd2f36102669fcfd0050e7a58c5abd)

build() {
	rm -rf build
	arch-meson "${pkgname}-${pkgver}" build -Duse_system_wfconfig=enabled -Duse_system_wlroots=enabled
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
