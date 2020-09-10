# Maintainer: Yiyao Yu <yuydevel at protonmail org>
# Contributor: Moritz Lipp <mlq@pwmt.org>

pkgname=bear
_pkgname=Bear
pkgver=2.4.4
pkgrel=1
pkgdesc="tool to generate compilation database for clang tooling"
arch=('i686' 'x86_64')
url="https://github.com/rizsotto/Bear"
license=('GPL3')
makedepends=('cmake' 'ninja')
depends=('python>=2.7')
options=('!ccache')
conflicts=('bear')
provides=('bear')
source=($_pkgname-$pkgver.tar.gz::https://github.com/rizsotto/$_pkgname/archive/$pkgver.tar.gz)
sha256sums=('5e95c9fe24714bcb98b858f0f0437aff76ad96b1d998940c0684c3a9d3920e82')

prepare() {
	cd "$srcdir/$_pkgname-$pkgver"
	mkdir -p build
}

build() {
	cd "$srcdir/$_pkgname-$pkgver/build"
	cmake \
		-GNinja \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCMAKE_INSTALL_SYSCONFDIR=/etc \
		-DCMAKE_BUILD_TYPE=plain \
		-DCMAKE_INSTALL_LIBDIR=lib \
		..
	cmake --build . -- -v
}

check() {
	cd "$srcdir/$_pkgname-$pkgver/build"
	cmake --build . -- -v check
}

package() {
	cd "$srcdir/$_pkgname-$pkgver/build"
	DESTDIR="$pkgdir" cmake --build . -- -v install
}
