# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

pkgname=qcm
pkgver=1.3.3
pkgrel=1
pkgdesc="Qt client for netease cloud music"
arch=('x86_64')
url="https://github.com/hypengw/Qcm"
license=('GPL-2.0-or-later')
depends=(
	'qt6-base'
	'qt6-declarative'
	'qt6-grpc'
	'qt6-shadertools'
	'hicolor-icon-theme'
	'curl'
	'openssl'
	'dbus'
	'ffmpeg'
	'cubeb'
	'kdsingleapplication'
	'qcmbackend'
	'qmlmaterial'
)
makedepends=(
	'git'
	'git-lfs'
	'clang'
	'lld'
	'cmake'
	'ninja'
	'asio'
	'pegtl'
	'vulkan-headers'
)
optdepends=('qcm-ncm-plugin: Netease Cloud Music plugin')
source=(
	"git+${url}.git#tag=v${pkgver}"
	"git+https://github.com/hypengw/rstd.git"
	"git+https://github.com/hypengw/ncrequest.git"
	"git+https://github.com/hypengw/kstore.git"
	"git+https://github.com/ilqvya/random.git"
	"fix-kdsingleapplication.patch"
)
sha256sums=('851c2edd37d9a85589321b8c3515625b830a5d120a87e103339e764171b970c3'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '08a3aa14c098044dd4a129a292558df4ecfaf7bbeec0b295e5d8009c5939c422')

prepare() {
	patch -d Qcm -Np1 -i ../fix-kdsingleapplication.patch
}

build() {
	cmake -B build \
		-S Qcm \
		-G Ninja \
		-D CMAKE_BUILD_TYPE=None \
		-D CMAKE_INSTALL_PREFIX=/usr \
		-D FETCHCONTENT_FULLY_DISCONNECTED=ON \
		-D FETCHCONTENT_SOURCE_DIR_RSTD="${srcdir}/rstd" \
		-D FETCHCONTENT_SOURCE_DIR_NCREQUEST="${srcdir}/ncrequest" \
		-D FETCHCONTENT_SOURCE_DIR_KSTORE="${srcdir}/kstore" \
		-D FETCHCONTENT_SOURCE_DIR_RANDOM="${srcdir}/random" \
		-D CMAKE_CXX_COMPILER=clang++ # Require clang 20+ to build

	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
}
