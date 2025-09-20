# Maintainer: xiretza <xiretza+aur@xiretza.xyz>
_pkgname=sgp4
pkgname=$_pkgname-git
pkgver=r301.ca9d4d9
pkgrel=1
pkgdesc="SGP4 library"
arch=(x86_64)
url="https://github.com/dnwrnr/sgp4"
license=('Apache')
depends=('gcc-libs')
makedepends=('cmake' 'git')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=('git+https://github.com/dnwrnr/sgp4.git')
sha256sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cmake -B build -S "$_pkgname" \
		-DCMAKE_BUILD_TYPE='None' \
		-DCMAKE_INSTALL_PREFIX=/usr
	make -C build
}

package() {
	make -C build DESTDIR="$pkgdir/" install
}
