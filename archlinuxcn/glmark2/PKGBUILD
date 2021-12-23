# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: farseerfc <farseerfc@gmail.com>
pkgname=glmark2
pkgver=2021.12
pkgrel=1
pkgdesc="An OpenGL 2.0 and ES 2.0 benchmark"
arch=('x86_64' 'aarch64')
url="https://github.com/glmark2/glmark2"
license=('GPL3' 'custom')
depends=('egl-wayland' 'libjpeg-turbo' 'libpng' 'libx11' 'mesa' 'systemd-libs')
makedepends=('meson' 'systemd' 'wayland-protocols')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('9f111284b2ef1d3fce91928e249e6ca00796a036831b063a549a0f3b03557a95')

build() {
  arch-meson "$pkgname-$pkgver" build \
    -Dflavors=drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2
  meson compile -C build
}

# No tests defined
#check() {
#  meson test -C build --print-errorlogs
#}

package() {
  meson install -C build --destdir "$pkgdir"

  cd "$pkgname-$pkgver"
  install -Dm644 COPYING.SGI -t "$pkgdir/usr/share/licenses/$pkgname"
}
