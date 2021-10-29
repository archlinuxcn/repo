# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20211029
_pkgver=${pkgver/+/-git-}
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv6h armv7h aarch64)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/experimental/$pkgname-$_pkgver.tar.gz)
sha512sums=('88ea872b1a9e34f3888155250983f136bdb970a8948b98f1e0703dd25e1b234d177ba6a7c8dcc45ace759b13bacd4aa361ee8bfe7e4f59855a53bee7667a8b7b')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
