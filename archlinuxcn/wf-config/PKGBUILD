# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=wf-config
pkgver=0.3
pkgrel=2
pkgdesc="A library for managing configuration files, written for wayfire"
arch=(x86_64)
url=https://wayfire.org
license=(custom:MIT)
depends=(libevdev 'wlroots>=0.8.0')
makedepends=(meson ninja pkg-config wayland-protocols)
conflicts=("${pkgname}-git")
source=("https://github.com/WayfireWM/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha512sums=('b0df9735583c0665fb2fdd2353dbce07e11239eb26fd080159c7f386dba9b370d7908b09504bafde1e11f45be95adc128466017c45e9fcd75a0dea00af70d741')

build() {
	rm -rf build
	arch-meson "${pkgname}-${pkgver}" build
	ninja -C build
}


package() {
	DESTDIR="${pkgdir}" ninja -C build install
}
