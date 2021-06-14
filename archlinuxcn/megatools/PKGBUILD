# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Ondrej Jirman <megous@megous.com>

pkgname=megatools
pkgver=1.11.0+20210505
_pkgver=${pkgver/+/-git-}
pkgrel=1
pkgdesc='CLI for MEGA'
arch=(i686 x86_64 armv7h)
url=https://megatools.megous.com
license=(GPL2)
depends=(curl glib2)
makedepends=(asciidoc docbook2x meson)
source=(https://megatools.megous.com/builds/experimental/$pkgname-$_pkgver.tar.gz)
sha512sums=('ef683129dd795f551718b99c40ea81a271a76c2f16bb6468a156c03236151883d4bd5daf4288f916b28b3b40ec9debc90d37342806e456b881bcb435b272c40b')

build() {
  arch-meson $pkgname-$_pkgver build -D symlinks=true -D man=true

  ninja -C build
}

package() {
  DESTDIR="$pkgdir" ninja -C build install
}
