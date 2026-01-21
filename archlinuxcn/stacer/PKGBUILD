# Maintainer: George Hu <integral@archlinux.org>
# Contributor: dundee
# Contributor: twa022 <twa022 at gmail dot com>

pkgname=stacer
_srcname=Stacer
pkgver=1.6.1
pkgrel=1
pkgdesc="Linux System Optimizer and Monitoring"
url="https://${pkgname}.quentium.fr/"
arch=('i686' 'x86_64' 'aarch64' 'riscv64')
license=('GPL-3.0-or-later')
depends=('qt6-base' 'qt6-charts' 'qt6-svg' 'hicolor-icon-theme')
makedepends=('cmake' 'qt6-tools')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/QuentiumYT/${_srcname}/archive/v${pkgver}.tar.gz")
sha256sums=('b534d343d5d47ac0195575fc6b1e1a266e5698419a3be4aa1d9ec685ef43b9b2')

build() {
	local cmake_options=(
		-B build
		-S "${_srcname}-${pkgver}"
		-W no-dev
		-D CMAKE_BUILD_TYPE=None
		-D CMAKE_INSTALL_PREFIX=/usr
	)

	cmake "${cmake_options[@]}"
	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
}
