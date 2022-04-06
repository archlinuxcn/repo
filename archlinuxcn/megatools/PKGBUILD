# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20220401
_pkgver=${pkgver/+/-git-}
pkgrel=2
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv6h armv7h aarch64)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/experimental/$pkgname-$_pkgver.tar.gz)
sha512sums=('198c9f74179b5b59ccf6728f6e086f66541f90bba355ba857f66850cceebe94566cf9619f35f66788cca47c24c70b7e4b8cd54c3d1e882a12883116411344c8b')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
