# Maintainer: Manuel Stoeckl <com dоt mstoeckl аt wppkgb>
pkgname=waypipe
pkgver=0.10.1
pkgrel=1
pkgdesc='A proxy for Wayland protocol applications; like ssh -X'
license=('MIT')
makedepends=('meson' 'ninja' 'scdoc' 'shaderc' 'pkgconf' 'cargo' 'rust-bindgen' 'clang' 'vulkan-headers')
depends=('lz4' 'zstd' 'vulkan-icd-loader' 'mesa' 'ffmpeg')
optdepends=(
	'openssh: recommended transport'
)
checkdepends=('vulkan-validation-layers')
url='https://gitlab.freedesktop.org/mstoeckl/waypipe'
source=("https://gitlab.freedesktop.org/mstoeckl/$pkgname/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz")
sha256sums=('43efc0d6bb54a13a3c9ee9f117cb20f20e64ba718ce059de5d0e8c07f3c60534')
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')

build() {
	cargo fetch --locked --manifest-path "$pkgname-v$pkgver/Cargo.toml"
	mkdir -p build
	meson build "$pkgname-v$pkgver" --buildtype debugoptimized -Dwerror=false --prefix /usr
	ninja -C build
}

package() {
	DESTDIR="$pkgdir" ninja -C "$srcdir/build" install
	install -Dm644 "$pkgname-v$pkgver/LICENSE.GPLv3" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
