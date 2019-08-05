# Maintainer: Jean Lucas <jean@4ray.co>

pkgname=sccache
pkgver=0.2.9
pkgrel=2
pkgdesc='ccache with cloud storage'
arch=(i686 x86_64)
url=https://github.com/mozilla/sccache
license=(Apache)
depends=(openssl)
makedepends=(cargo openssl-1.0)
source=(sccache-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha512sums=('289109338913c935752e9bbcd45b7bf4ef48be03b5a7d92c93ac220b98f04338ff562030cf126f80bda8db41e83b1103e6c2bd55caaeef4d7804157f4f685080')

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
  rm "$pkgdir"/usr/.crates.toml
  install -Dm 644 README.md -t "$pkgdir"/usr/share/doc/sccache
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/sccache
}
