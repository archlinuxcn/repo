# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Caleb Maclennan <caleb@alerque.com>

pkgname=resvg
pkgver=0.31.1
pkgrel=1
pkgdesc='SVG rendering library and CLI'
arch=(i686 x86_64)
url="https://github.com/RazrFalcon/$pkgname"
license=(MPL2)
depends=(gdk-pixbuf2)
optdepends=(
	'qt5-base: For the Qt backend'
	'cairo: For the cairo backend'
	'kio: For the dolphin thumbnailer'
)
makedepends=(cargo clang qt5-base qt5-tools kio cairo pango cmake extra-cmake-modules)
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('a2f09d00e4e0d689c72924dac46aa21371e89c751344051ead08397e2cf644c8')

prepare() {
	cd "$pkgname-$pkgver"
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
	mkdir -p tools/kde-dolphin-thumbnailer/build
}

build() {
	cd "$pkgname-$pkgver"
	
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --workspace --frozen --release --all-features
	
	(
		cd tools/viewsvg
		qmake PREFIX="$pkgdir/usr"
		make
	)
	
	(
		cd tools/kde-dolphin-thumbnailer/build
		cmake .. \
			-Wno-dev \
			-DCMAKE_CXX_FLAGS="-L../../../target/release" \
			-DCMAKE_INSTALL_PREFIX="$pkgdir/$(qtpaths --install-prefix)" \
			-DQT_PLUGIN_INSTALL_DIR="$pkgdir/$(qtpaths --plugin-dir)" \
			-DCMAKE_BUILD_TYPE=Release
		make
	)
	
	cargo doc --release --no-deps -p resvg-capi
}

check() {
	cd "$pkgname-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$pkgname-$pkgver"
	install -Dm755 -t "$pkgdir/usr/bin/" target/release/{resvg,usvg} tools/viewsvg/viewsvg
	make -C tools/kde-dolphin-thumbnailer/build install
	install -Dm755 -t "$pkgdir/usr/lib/" target/release/libresvg.so
	install -Dm644 -t "$pkgdir/usr/include/" c-api/*.h
	install -d "$pkgdir/usr/share/doc/resvg"
	cp -r target/doc/* "$pkgdir/usr/share/doc/resvg"
}
