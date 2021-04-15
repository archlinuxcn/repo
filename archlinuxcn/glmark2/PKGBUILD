# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: farseerfc <farseerfc@gmail.com>
pkgname=glmark2
pkgver=2021.02
pkgrel=1
pkgdesc="An OpenGL 2.0 and ES 2.0 benchmark"
arch=('x86_64')
url="https://github.com/glmark2/glmark2"
license=('GPL' 'custom')
depends=('egl-wayland' 'libjpeg-turbo' 'libpng' 'libx11' 'mesa' 'systemd-libs')
makedepends=('meson' 'systemd' 'wayland-protocols')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('bebadb78c13aea5e88ed892e5563101ccb745b75f1dc86a8fc7229f00d78cbf1')

build() {
	arch-meson "$pkgname-$pkgver" build \
		-Dflavors=drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2
	meson compile -C build
}

package() {
	DESTDIR="$pkgdir" meson install -C build

	cd "$pkgname-$pkgver"
	install -Dm644 COPYING.SGI -t "$pkgdir/usr/share/licenses/$pkgname"
}
