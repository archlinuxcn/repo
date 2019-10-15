# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wayfire
pkgver=0.3
pkgrel=1
pkgdesc="3D wayland compositor"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(cairo 'wf-config>=0.3' glm libjpeg)
makedepends=(meson ninja wayland-protocols)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/${pkgver}.0/${pkgname}-${pkgver}.tar.xz")
sha256sums=('09c54ed81030dadebdd624eb0546f332af0f96b9e91149eb0c1cdbb99143fe86')
sha512sums=('096d03795d56d336857e844ec9cef68af36c11d1d5dc7e591aaf9be54bf1a58a87e4c23624da58d71a5fe3056a11ffc3e788316ef01fb8c36b862378065ce31a')

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
