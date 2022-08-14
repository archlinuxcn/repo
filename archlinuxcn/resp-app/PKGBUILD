# Maintainer: Zhanibek Adilbekov <zhanibek.adilbekov@pm.me>
# Maintainer: Versus Void <chaoskeeper &commat; mail FULL STOP ru>
# Maintainer: Mehmet Ozgur Bayhan <mozgurbayhan@gmail.com>
# Contributor: Vyacheslav Konovalov <echo dnlhY2hrb25vdmFsb3ZAZ21haWwuY29tCg== | base64 -d>

pkgname=resp-app
pkgver=2022.4.2
pkgrel=1
pkgdesc='RESP.app - Open source cross-platform Redis Desktop Manager GUI based on Qt 5'
arch=('x86_64')
url="https://resp.app"
license=('GPL3')
depends=(
	'qt5-base'
	'qt5-imageformats'
	'qt5-tools'
	'qt5-declarative'
	'qt5-quickcontrols'
	'qt5-quickcontrols2'
	'qt5-charts'
	'qt5-graphicaleffects'
	'qt5-svg'
	'libssh2'
	'python')
makedepends=('git' 'gcc' 'make' 'cmake')
provides=('redis-desktop-manager')
source=("resp::git+https://github.com/uglide/RedisDesktopManager.git#tag=$pkgver"
	'resp.desktop')
sha256sums=('SKIP'
            '02ec9ed57fbf08b254db8e1a9fa92476253dfe2505d687a5738ea1867a75d28b')

prepare() {
	cd resp/
	git submodule update --init --recursive
}

build() {
	cd "$srcdir/resp/3rdparty/lz4/build/cmake"
	cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DLZ4_BUNDLED_MODE=ON . && make
	cd "$srcdir/resp/3rdparty/zstd/build/cmake"
	cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release . && make libzstd_static
	cd "$srcdir/resp/3rdparty/snappy"
	cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release -DSNAPPY_BUILD_BENCHMARKS=0 . && make
	cd "$srcdir/resp/3rdparty/brotli"
	cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_BUILD_TYPE=Release . && make
	cd "$srcdir/resp/src"
	lrelease resp.pro
	qmake VERSION="$pkgver" && make
}

package() {
	_instdir="$srcdir/resp/bin/linux/release"
	_bindir="$pkgdir/usr/share/$pkgname/bin"

	mkdir -p "${_bindir}"
	mkdir "$pkgdir/usr/share/licenses"
	mkdir "$pkgdir/usr/share/pixmaps"
	mkdir "$pkgdir/usr/share/applications"

	install -Dm644 "$srcdir/resp/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm755 "${_instdir}/resp" "${_bindir}/resp"
	install -Dm644 "$srcdir/resp/src/resources/images/resp.png" "$pkgdir/usr/share/pixmaps/resp.png"
	install -Dm644 "$srcdir/resp.desktop" "$pkgdir/usr/share/applications/resp.desktop"

	mkdir "$pkgdir/usr/bin"
	ln -s "/usr/share/$pkgname/bin/resp" "$pkgdir/usr/bin/resp"
}
