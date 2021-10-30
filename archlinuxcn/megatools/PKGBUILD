# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20211030
_pkgver=${pkgver/+/-git-}
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv6h armv7h aarch64)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/experimental/$pkgname-$_pkgver.tar.gz)
sha512sums=('29b23cd647bf1b53823927f58a33cc3b357a659751eca8a1d4a3b8837e127dfc5852a32f2f7ccb6fc274d5f7d30fc3e8d6d5f846d7790f4441598ef4f082064f')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
