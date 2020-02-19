# Maintainer: Chocobo1 <chocobo1 AT archlinux DOT net>
# Former maintainer: Jean Lucas <jean@4ray.co>

pkgname=sccache
pkgver=0.2.12
pkgrel=3
pkgdesc="Shared compilation cache"
arch=('i686' 'x86_64')
url="https://github.com/mozilla/sccache"
license=('apache')
depends=('openssl')
makedepends=('rust')
#checkdepends=('openssl-1.0')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mozilla/sccache/archive/$pkgver.tar.gz")
sha256sums=('591a82ddbc2e970630a9426c78c25cbc52c3261b06d57cb4e1f11ab8008629fa')


check() {
  cd "$pkgname-$pkgver"

  #OPENSSL_LIB_DIR="/usr/lib/openssl-1.0" \
  #  OPENSSL_INCLUDE_DIR="/usr/include/openssl-1.0" \
  #  cargo test --release
}

package() {
  cd "$pkgname-$pkgver"

  cargo install --root "$pkgdir/usr" --path "$srcdir/$pkgname-$pkgver"
  install -Dm644 "README.md" -t "$pkgdir/usr/share/doc/sccache"

  rm -f "$pkgdir/usr"/.crates*
}
