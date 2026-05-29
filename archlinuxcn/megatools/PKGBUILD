# Maintainer: 
# Contributor: T.J. Townsend <blakkheim@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.12.0
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(x86_64)
url='https://xff.cz/megatools'
license=(GPL-2.0-only)
depends=(curl glib2)
makedepends=(asciidoc docbook2x git meson)
source=(git+https://xff.cz/git/megatools?signed#tag=${pkgver})
sha256sums=('cc141f1b501283ea3bfc1955acad09142649565809e3db1ddf3c48f64960d961')
validpgpkeys=(EBFBDDE11FB918D44D1F56C1F9F0A873BE9777ED) # Ondrej Jirman <megous@megous.com>

build() {
  arch-meson $pkgname build -D symlinks=true -D man=true
  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
