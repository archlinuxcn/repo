# Maintainer: Alexandre Bouvier <contact@amb.tf>
_pkgname=discord-rpc
pkgname=$_pkgname-git
pkgver=3.4.0.r10.g963aa9f
pkgrel=4
pkgdesc="Discord Rich Presence library"
arch=('aarch64' 'armv7h' 'i486' 'i686' 'pentium4' 'x86_64')
url="https://github.com/discord/discord-rpc"
license=('MIT')
depends=('gcc-libs')
makedepends=('cmake' 'git' 'rapidjson>=1.1')
provides=("$_pkgname=$pkgver" 'libdiscord-rpc.so')
conflicts=("$_pkgname")
source=("$_pkgname::git+$url.git")
b2sums=('SKIP')

pkgver() {
	cd $_pkgname
	git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cmake -S $_pkgname -B build \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
		-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Wno-dev
	cmake --build build
}

package() {
	# shellcheck disable=SC2154
	DESTDIR="$pkgdir" cmake --install build
	install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname $_pkgname/LICENSE
}
