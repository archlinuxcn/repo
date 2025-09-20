# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
_pkgname=libsigmf
pkgname=$_pkgname-git
pkgver=r18.94445d4
pkgrel=1
pkgdesc="A header-only C++ library for working with SigMF metadata"
arch=(any)
url="https://github.com/deepsig/libsigmf"
license=('Apache')
depends=()
makedepends=('cmake' 'git' 'flatbuffers' 'nlohmann-json')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("git+$url.git"
)
sha256sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
	cd "$_pkgname"
}

build() {
	cmake -B build -S "$_pkgname" \
		-Wno-dev \
		-DCMAKE_BUILD_TYPE='None' \
		-DUSE_SYSTEM_FLATBUFFERS=ON \
		-DUSE_SYSTEM_JSON=ON \
		-DCMAKE_INSTALL_PREFIX=/usr
	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir/" install
}
