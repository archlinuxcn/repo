# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
pkgname=drm_info
pkgver=2.7.0
pkgrel=1
license=(MIT)
pkgdesc='Small utility to dump info about DRM devices'
makedepends=(meson scdoc)
depends=("libdrm>=2.4.115" json-c pciutils)
arch=(x86_64 aarch64)
url=https://gitlab.freedesktop.org/emersion/drm_info
conflicts=(drm_info-git)
source=("${url}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.bz2")
b2sums=('59c049613aebada228fa4a99af0baff60b5a4db8ce849b0ad59b0e4b1e0471306f5051c0962197d01fc4a06a603fcff14b5c0ce1a8013166758e398ef1f8a320')

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
