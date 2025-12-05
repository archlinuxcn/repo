# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=qmlmaterial-git
_pkgname=${pkgname%-git}
_srcname=QmlMaterial
pkgver=0.1.3.r46.g0451915
pkgrel=1
pkgdesc="Material Design 3 for QML"
arch=('x86_64')
url="https://github.com/hypengw/${_srcname}"
license=('MIT')
depends=('qt6-base' 'qt6-declarative' 'qt6-shadertools')
makedepends=('git' 'git-lfs' 'cmake')
provides=("${_pkgname}" "libqml_material.so")
conflicts=("${_pkgname}")
source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
	cd "${_srcname}/"
	git describe --long --tags --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

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
