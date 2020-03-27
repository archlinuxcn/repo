# Maintainer: Chocobo1 <chocobo1 AT archlinux DOT net>
# Former maintainer: Jean Lucas <jean@4ray.co>

pkgname=sccache
pkgver=0.2.13
pkgrel=4
pkgdesc="Shared compilation cache"
arch=('i686' 'x86_64')
url="https://github.com/mozilla/sccache"
license=('apache')
depends=('openssl' 'zlib')
makedepends=('rust')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mozilla/sccache/archive/$pkgver.tar.gz")
sha256sums=('81c973cf9a89e77f02a6b5710298531ba2e50d2555e8a931e505fbf570522e2a')


check() {
  cd "$pkgname-$pkgver"

  #cargo test \
  #  --release \
  #  --locked \
  #  --all-features
}

package() {
  cd "$pkgname-$pkgver"

  cargo install \
    --no-track \
    --locked \
    --root "$pkgdir/usr" \
    --path "$srcdir/$pkgname-$pkgver" \
    --all-features

  install -Dm644 "README.md" -t "$pkgdir/usr/share/doc/sccache"
}
