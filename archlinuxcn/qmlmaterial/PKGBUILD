# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=qmlmaterial
_srcname=QmlMaterial
pkgver=0.1.4
pkgrel=2
pkgdesc="Material Design 3 for QML"
arch=('x86_64')
url="https://github.com/hypengw/${_srcname}"
license=('MIT')
depends=('qt6-base' 'qt6-declarative' 'qt6-shadertools')
makedepends=('git' 'git-lfs' 'cmake')
provides=('libqml_material.so')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('2382534d8be7f4ca74395d60aff3c69a2adee718ed0f2c6fbf67e54633bd1cd6')

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
