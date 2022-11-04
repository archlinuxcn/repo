# Maintainer: Alexandre Bouvier <contact@amb.tf>
_pkgname=zarchive
pkgname=$_pkgname-git
pkgver=0.1.2.r0.gd2c7177
pkgrel=1
pkgdesc="Library for creating and reading zstd-compressed file archives"
arch=('aarch64' 'armv7h' 'i486' 'i686' 'pentium4' 'x86_64')
url="https://github.com/Exzap/ZArchive"
license=('MIT')
makedepends=('cmake>=3.15' 'git' 'zstd')
provides=("$_pkgname=$pkgver" 'libzarchive.so')
conflicts=("$_pkgname")
source=("$_pkgname::git+$url.git")
b2sums=('SKIP')

pkgver() {
	cd $_pkgname
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cmake -S $_pkgname -B shared \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
		-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Wno-dev
	cmake --build shared
}

package() {
	depends+=('libzstd.so')
	# shellcheck disable=SC2154
	DESTDIR="$pkgdir" cmake --install shared
	install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname $_pkgname/LICENSE
}
