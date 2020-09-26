# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20200830
_pkgver=${pkgver/+/-git-}
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv7h)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/experimental/$pkgname-$_pkgver.tar.gz)
sha512sums=('a64158b7248ea99d72b1aa790c28deb00ceca3065396565b187e371c415b27c05d782df45bd2f41bfae0b7439c303c4b44d820ea7c44b5fa733dbdf70d68cfa8')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
