# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

pkgname=qcm
pkgver=1.3.0
pkgrel=2
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
	'git-lfs'
	'clang'
	'cmake'
	'ninja'
	'asio'
	'pegtl'
	'vulkan-headers'
)
optdepends=('qcm-ncm-plugin-git: Netease Cloud Music plugin')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('cd2cdea3c2e1340bb36cb7446b89acef3940afe39032aef07e2451bf378f62d1')

prepare() {
	git lfs install
}

build() {
	cmake -B build \
		-S Qcm \
		-G Ninja \
		-D CMAKE_BUILD_TYPE=None \
		-D CMAKE_INSTALL_PREFIX=/usr \
		-D CMAKE_CXX_COMPILER=clang++ # Require clang 20+ to build

	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
}
