# Maintainer: Jean Lucas <jean@4ray.co>

pkgname=sccache
pkgver=0.2.10
pkgrel=1
pkgdesc='ccache with cloud storage'
arch=(i686 x86_64)
url=https://github.com/mozilla/sccache
license=(Apache)
depends=(openssl)
makedepends=(cargo openssl-1.0)
source=(sccache-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha512sums=('4f4c051e93d937bae42739d9030dddddde48af59d66c69256172ad660e8d6135c64a77421174b98d304ddff9949d33a04e84e05c255ceccc73cd9cab32663989')

build() {
  cd sccache-$pkgver
  cargo build --release
}

check() {
  cd sccache-$pkgver
  # native-tls crate depends on older openssl crate
  OPENSSL_LIB_DIR=/usr/lib/openssl-1.0 \
    OPENSSL_INCLUDE_DIR=/usr/include/openssl-1.0 \
    cargo test --release
}

package() {
  cd sccache-$pkgver

  cargo install --path . --root "$pkgdir"/usr
  rm "$pkgdir"/usr/.crates.toml # Remove unneeded file

  install -Dm 644 README.md -t "$pkgdir"/usr/share/doc/sccache
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/sccache
}
