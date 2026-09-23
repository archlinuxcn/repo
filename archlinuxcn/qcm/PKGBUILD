# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

# See lito.lock
_ncrequest_commit=cdaca8b5c523906fc0c9ed58cd5f2c7981b5a255
_qextra_commit=68f752fd38e3d7a923bf36d621f4a94be7b26fd8
_random_commit=567e9c62df20f19adbda0e12fa4d88b2b49a7d1c
_wavsen_commit=ad8a0f6dab8bf280c0be2836cdf6f22416d8b1d1
_vvk_commit=117626d9bfc6c1de0f2957f7fa42b47935bb6af8
_rstd_version=0.1.3

pkgname=qcm
pkgver=1.3.5
pkgrel=2
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
	'qmlmaterial'
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
optdepends=('qcm-ncm-plugin: Netease Cloud Music plugin')
replaces=('qcmbackend')
source=(
	"git+${url}.git#tag=v${pkgver}"
	"git+https://github.com/hypengw/ncrequest.git#commit=${_ncrequest_commit}"
	"git+https://github.com/hypengw/QExtra.git#commit=${_qextra_commit}"
	"git+https://github.com/ilqvya/random.git#commit=${_random_commit}"
	"git+https://github.com/hypengw/wavsen.git#commit=${_wavsen_commit}"
	"git+https://github.com/litocpp/vvk.git#commit=${_vvk_commit}"
	"git+https://github.com/litocpp/rstd.git#tag=v${_rstd_version}"
)
sha256sums=('6cca08f3c04287557e436161bd08de2db3c0f791b60abc8b086e5fd0cdf85369'
            'e0b29a7179d1f35b76ca2582003c0a97c20b1a30b8e2e24cd95b025e7bfabfca'
            '2b2d0a9f7031c88656fde765e7118960486db25aff5ceff43d71a1c3737643ac'
            '0fec05e02154c94be675e16905fd0aad0d641bfeab96b006535cff508b905180'
            '6b739d364463672474652916f3b57c0b191d5dbbdce20433d1f17cff9220b3ac'
            'f49079a367c7759207d56d49789f5f7c0bfa99b1a3d204566aeceddd9f097b67'
            'ebf0fd9b60d85a7f465992a75b581b7141bfd2102d8c4f752dada017dc2b74a7')

prepare() {
	cd Qcm

	# Allow using system dependencies
	git cherry-pick -n d82610e55acf942f271bd92d3d495aa218148aed

	mkdir -p .lito
	cat >.lito/config.toml <<END
[patch."https://github.com/hypengw/ncrequest.git"]
path = "../ncrequest"

[patch."https://github.com/hypengw/QExtra.git"]
path = "../QExtra"

[patch."https://github.com/ilqvya/random.git"]
path = "../random"

[patch."https://github.com/hypengw/wavsen.git"]
path = "../wavsen"

[patch."https://github.com/litocpp/rstd.git"]
path = "../rstd"

[patch."https://github.com/litocpp/vvk.git"]
path = "../vvk"

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
