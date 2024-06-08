# Maintainer: Jeremy Gust <jeremy AT plasticsoup DOT net>
pkgname=hyprpicker
pkgver=0.3.0
pkgrel=1
pkgdesc="A wlroots-compatible Wayland color picker that does not suck."
arch=(x86_64)
url="https://github.com/hyprwm/hyprpicker"
license=('BSD-3-Clause')
depends=('cairo' 'gcc-libs' 'glibc' 'libxkbcommon' 'wayland')
optdepends=('wl-clipboard: Allows --autocopy to automatically copy the output to the clipboard.')
makedepends=('cmake'
             'libglvnd'
             'libjpeg-turbo'
             'ninja'
             'pango'
             'wayland-protocols'
             'wlroots')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('a443188ef7619be48c9992ea208121772b7e1da6662d672c650e30e159eeb891')

build() {
	export CC=gcc
	export CXX=g++
	cmake -B build -S "$pkgname-$pkgver" \
		-DCMAKE_BUILD_TYPE='None' \
		-DCMAKE_INSTALL_PREFIX='/usr' \
		-Wno-dev
	cmake --build build
}

package() {
	install -Dm755 build/hyprpicker "${pkgdir}/usr/bin/hyprpicker"
	cd "$pkgname-$pkgver"
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 doc/hyprpicker.1 "${pkgdir}/usr/share/man/man1/hyprpicker.1"
	install -Dm644 README.md "${pkgdir}/usr/share/doc/$pkgname/README.md"
}
