# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=drm_info
pkgver=2.8.0
pkgrel=1
license=(MIT)
pkgdesc='Small utility to dump info about DRM devices'
makedepends=(meson scdoc)
depends=("libdrm>=2.4.115" json-c pciutils)
arch=(x86_64 aarch64)
url=https://gitlab.freedesktop.org/emersion/drm_info
conflicts=(drm_info-git)
source=("${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.bz2")
b2sums=('3b481f0342109d4852ecd756e3de985f684ce870457755ebede213020378f3f0daf046a2403fa16a69c451878bc0870789bdfe2c57ee5b8c66dee48e225d876c')

build() {
	rm -rf build
	arch-meson build "${pkgname}-v${pkgver}" -Dlibpci=enabled -Dman-pages=enabled
	meson compile -C build
}

check () {
	meson test -C build
}

package() {
	meson install -C build --destdir="${pkgdir}"
	install -Dm644 "${pkgname}-v${pkgver}/LICENSE" \
		"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
