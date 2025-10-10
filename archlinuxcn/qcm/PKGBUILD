# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

pkgname=qcm
pkgver=1.3.0
pkgrel=1
pkgdesc="Qt client for netease cloud music"
arch=('x86_64')
url="https://github.com/hypengw/Qcm"
license=('GPL-2.0-or-later')
depends=(
	'qt6-base'
	'qt6-quick3d'
	'qt6-grpc'
	'hicolor-icon-theme'
	'curl'
	'openssl'
	'dbus'
	'ffmpeg'
	'fmt'
	'cubeb-git'
	'kdsingleapplication'
	'qcmbackend-git'
)
makedepends=(
	'git'
	'clang'
	'cmake'
	'ninja'
	'asio'
	'pegtl'
	'vulkan-headers'
)
optdepends=('qcm-ncm-plugin-git: Netease Cloud Music plugin')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('e441f3b5172c93b365a977e96a95873fd75831e51c07fd429d9f2fcb37685318')

build() {
	cmake -B build \
		-S "Qcm-${pkgver}" \
		-G Ninja \
		-D CMAKE_BUILD_TYPE=None \
		-D CMAKE_INSTALL_PREFIX=/usr \
		-D CMAKE_CXX_COMPILER=clang++ # Require clang 20+ to build

	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
}
