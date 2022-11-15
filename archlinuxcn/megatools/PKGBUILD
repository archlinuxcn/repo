# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20220519
_pkgver=${pkgver/+/.}
pkgrel=2
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv6h armv7h aarch64)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/$pkgname-$_pkgver.tar.gz)
sha512sums=('5c379a5a8da150d6d95a84f6bcf0c9be5b725c2c0e799e8d1e3358ac6081579eacc853f6b3d369c06006d3bdb3917dc20cf39ca5c69f153dc38de9daab74cea1')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
