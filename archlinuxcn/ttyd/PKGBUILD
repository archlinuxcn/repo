# Submitter: Daniel M. Capella <polyzen@archlinux.org>
# Maintainer: Elmar Klausmeier <Elmar.Klausmeier@gmail.com>

pkgname=ttyd
pkgver=1.7.1
pkgrel=1
pkgdesc='Share your terminal over the web'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url=https://tsl0922.github.io/ttyd/
license=('MIT')
depends=('json-c' 'libpcap' 'libwebsockets' 'zlib')
makedepends=('cmake')
source=("ttyd.service"
	"https://raw.githubusercontent.com/eklausme/c/master/slogin.c"
	"https://github.com/tsl0922/ttyd/archive/$pkgver/ttyd-$pkgver.tar.gz")
sha512sums=('b6c731444ad78d68464082557a4b7dae857f2b86511810f055d2a4c8e1c7051328cdbcd1f8a43c322a2dd20c20474b483f9fa104785268bafdefb04cce54287d'
            '1cebf87e06f6303c48d931a87614f05d7300b4fba45ac5bf5a56ac20a0c9f48a1997bce13611ab3b498eed991a74594318c49ae801595fc882755dc1928640bb'
            '1c69a320fb709bf59a1525664b9238129add88219d27ce7b15572604d74bab820197b954f65aeb2793c02705dd8e25e13bfdeb17378ef79724764ada81aa1517')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"/src
	mv server.c server.c.0
	sed 's/  info.ws_ping_pong_interval = 5/\/\/   info.ws_ping_pong_interval = 5/' server.c.0 > server.c
}

build() {
	cc -Wall slogin.c -o slogin -lpam -lpam_misc -lutil
	cd ttyd-$pkgver
	mv CMakeLists.txt CMakeLists.txt.0
	sed -e 's/find_package(Libwebsockets 1.7.0 QUIET)/find_package(Libwebsockets 4.3.1...<5.0.0 QUIET)/'	\
	    -e 's/cmake_minimum_required(VERSION 2.8)/cmake_minimum_required(VERSION 3.19)/'	\
	    CMakeLists.txt.0 > CMakeLists.txt
	mkdir -p build && cd build
	cmake -DCMAKE_INSTALL_PREFIX=/usr ..
	make
}

package() {
	cd ttyd-$pkgver/build
	make DESTDIR="$pkgdir" install

	install -Dm644 -t "$pkgdir"/usr/share/licenses/ttyd ../LICENSE

	# Install SystemD related files
	install -D -m644 ../../ttyd.service   "${pkgdir}/usr/lib/systemd/system/ttyd.service"

	# Install simplified login devoid of signal-handling
	install -D -m755 ../../slogin	"${pkgdir}/usr/bin/slogin"
}

