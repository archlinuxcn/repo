# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=qmlmaterial
_srcname=QmlMaterial
pkgver=0.1.3
pkgrel=1
pkgdesc="Material Design 3 for QML"
arch=('x86_64')
url="https://github.com/hypengw/${_srcname}"
license=('MIT')
depends=('qt6-base' 'qt6-declarative' 'qt6-shadertools')
makedepends=('git' 'git-lfs' 'cmake')
provides=('libqml_material.so')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('712b5079f64ec715331b08c0523eeef0017e7761a1179d368329c9b0b337298f')

prepare() {
	cd "${_srcname}/"
	git lfs install --local
	git remote add network-origin "${url}.git"
	git lfs pull network-origin
}

build() {
	local cmake_options=(
		-B build
		-S "${_srcname}"
		-D CMAKE_BUILD_TYPE=None
		-D CMAKE_INSTALL_PREFIX=/usr
	)

	cmake "${cmake_options[@]}"
	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
	install -Dm644 "${_srcname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
