# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Kimiblock Zhou <pn3535 at icloud dot com>

# Fix build with lito 0.8.5
_qcm_commit=69643b0ec91600f45a45142c71be35bb2ff87ac6

# See lito.lock
_ncrequest_commit=40d40224842a080039d2a76710fbedb20ee002ac
_qextra_commit=650cb670c15c2f34a9cf0dedd52447df7b56e761
_qmlmaterial_commit=98b8acd3e0bd57ca0710f2712e4dfa3fcef13113
_random_commit=567e9c62df20f19adbda0e12fa4d88b2b49a7d1c
_wavsen_commit=bd8a72e0f68fabc42f3d123623787398ed28dbe4
_vvk_version=0.1.0
_rstd_version=0.1.7

pkgname=qcm
pkgver=1.3.5
pkgrel=4
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
	'qt6-shadertools'
	'qt6-websockets'
	'hicolor-icon-theme'
	'openssl'
	'ffmpeg'
	'kdsingleapplication'
	'sqlite'
)
makedepends=(
	'git'
	'git-lfs'
	'cargo'
	'clang'
	'lito'
	'lld'
	'llvm'
	'cmake'
	'ninja'
	'vulkan-headers'
)
optdepends=('qcm-ncm-plugin: Netease Cloud Music plugin')
replaces=('qcmbackend')
source=(
	#"git+${url}.git#tag=v${pkgver}"
	"git+${url}.git#commit=${_qcm_commit}"
	"git+https://github.com/hypengw/ncrequest.git#commit=${_ncrequest_commit}"
	"git+https://github.com/hypengw/QExtra.git#commit=${_qextra_commit}"
	"git+https://github.com/hypengw/QmlMaterial.git#commit=${_qmlmaterial_commit}"
	"git+https://github.com/ilqvya/random.git#commit=${_random_commit}"
	"git+https://github.com/hypengw/wavsen.git#commit=${_wavsen_commit}"
	"git+https://github.com/litocpp/vvk.git#tag=v${_vvk_version}"
	"git+https://github.com/litocpp/rstd.git#tag=v${_rstd_version}"
)
sha256sums=('95dfe3440b23e00453742a18b33e4290e14de963381ae862faeeff457a85f0cc'
            '4d769781149aa7b321e7345e921e88cfc71e2598bffe0d5ceeb04e72f13371b1'
            '554a0e04a20a36614d6527a24cfff5491326dfd4a60905939d550449b7ef5b0e'
            'fc7ebd991227221d63597cc67bcf1ae7e2db03ae8bd6975aabf4a9f54ad2f218'
            '0fec05e02154c94be675e16905fd0aad0d641bfeab96b006535cff508b905180'
            '04856be2a686da2afb0c9972f76aeff89c32abeb535135553b062e1c05d99a2c'
            'f99a7c4993b7f00ba1d23b5c8777c7d924eae41cea17fca2ad032bc9e073568a'
            '499ce8606108d11a59f5d8b322b75cf3e8fe3e7e9f71eb4e81529f379eed7ade')

prepare() {
	pushd QmlMaterial
	git lfs install --local
	git remote add network-origin "https://github.com/hypengw/QmlMaterial.git"
	git lfs pull network-origin
	popd

	cd Qcm

	mkdir -p .lito
	cat >.lito/config.toml <<END
[patch."https://github.com/hypengw/ncrequest.git"]
path = "../ncrequest"

[patch."https://github.com/hypengw/QExtra.git"]
path = "../QExtra"

[patch."https://github.com/hypengw/QmlMaterial.git"]
path = "../QmlMaterial"

[patch."https://github.com/ilqvya/random.git"]
path = "../random"

[patch."https://github.com/hypengw/wavsen.git"]
path = "../wavsen"

[patch."https://github.com/litocpp/rstd.git"]
path = "../rstd"

[patch."https://github.com/litocpp/vvk.git"]
path = "../vvk"

[tools.cmake.overrides.KDSingleApplication]
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
