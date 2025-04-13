# Maintainer: 
# Contributor: T.J. Townsend <blakkheim@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.4
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(x86_64)
url='https://xff.cz/megatools'
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x git meson)
source=(git+https://xff.cz/git/megatools?signed#tag=${pkgver})
sha256sums=('8fb789b4ddcab79a02657e39296279ea88102058666095f39fbc2e4ffd63dcce')
validpgpkeys=(EBFBDDE11FB918D44D1F56C1F9F0A873BE9777ED) # Ondrej Jirman <megous@megous.com>

build() {
  arch-meson $pkgname build -D symlinks=true -D man=true
  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
