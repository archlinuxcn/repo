# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wayfire
pkgver=0.3.1
pkgrel=1
pkgdesc="3D wayland compositor"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(cairo 'wf-config>=0.3' glm libjpeg)
makedepends=(meson ninja wayland-protocols)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz"
        wlroots-0.10.patch)
sha256sums=('f7d51e6a65a2369d9dba9cbb90a2b3926cb0c919c0dc4f90fc078caad94f0a7f'
            '83a4194cbf24b5c1db2ed0cfec3406862fe219df79d7074c2b264670f58be886')

prepare () {
	cd "${pkgname}-${pkgver}"
	patch -p1 < "${srcdir}/wlroots-0.10.patch"
}

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
