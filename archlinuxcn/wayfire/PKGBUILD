# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wayfire
pkgver=0.2
pkgrel=1
pkgdesc="3D wayland compositor"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(cairo wf-config glm libjpeg)
makedepends=(meson ninja wayland-protocols)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=('f4d0b43b31e018aa711ed18d939758c7ad106212dd95c8d2445cf18778fdb34d')
sha512sums=('6803ad0fd3850833c644d4dbd535daad52a0ff6e539e041d41f812ecf671a37a71b3962c3272f2ab2dcf0043efb6526d2be85ad5ac161b8801a5e53717588883')

build() {
	rm -rf build
	arch-meson "${pkgname}-${pkgver}" build
	ninja -C build
}

package() {
	DESTDIR="${pkgdir}/" ninja -C build install
	cd "${pkgname}-${pkgver}"
	install -Dm644 wayfire.desktop "${pkgdir}/usr/share/wayland-sessions/wayfire.desktop"
	install -Dm644 wayfire.ini.default "${pkgdir}/usr/share/doc/${pkgname}/wayfire.ini.default"
	install -Dm645 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
