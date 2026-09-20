# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

pkgname=qcm-git
_pkgname=${pkgname%-git}
pkgver=1.3.5.r2.g24be634
pkgrel=1
pkgdesc="Qt client for netease cloud music"
arch=('x86_64')
url="https://github.com/hypengw/Qcm"
license=('GPL-2.0-or-later')
depends=(
	'glibc'
	'libstdc++'
	'libgcc'
	'qt6-base'
	'qt6-declarative'
	'qt6-grpc'
	'qt6-websockets'
	'hicolor-icon-theme'
	'openssl'
	'ffmpeg'
	'kdsingleapplication'
	'qmlmaterial-git'
	'sqlite'
)
makedepends=(
	'git'
	'cargo'
	'clang'
	'lito'
	'lld'
	'llvm'
	'cmake'
	'ninja'
	'vulkan-headers'
	'vulkan-memory-allocator'
)
optdepends=('qcm-ncm-plugin-git: Netease Cloud Music plugin')
replaces=('qcmbackend-git')
provides=("${_pkgname}")
conflicts=("${_pkgname}")
source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
	git -C Qcm describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/v//'
}

prepare() {
	cd Qcm
	mkdir -p .lito
	cat >.lito/config.toml <<END
[tools.cmake.overrides.qml_material]
source = "installed"

[tools.cmake.overrides.KDSingleApplication]
source = "installed"

[tools.cmake.overrides.VulkanMemoryAllocator]
source = "installed"
END

	lito fetch --all-features
}

build() {
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	CFLAGS+=" -ffat-lto-objects"

	# https://github.com/llvm/llvm-project/issues/121709
	CXXFLAGS="${CXXFLAGS//-Wp,-D_FORTIFY_SOURCE=3/}"
	lito -C Qcm build --frozen --profile plain --use-env-flags
}

package() {
	lito -C Qcm install --profile plain --prefix "${pkgdir}/usr" --no-build
}
