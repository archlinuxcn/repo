# Maintainer: Jean Lucas <jean@4ray.co>

pkgname=sccache
pkgver=0.2.12
pkgrel=2
pkgdesc='ccache with cloud storage'
arch=(x86_64 aarch64)
url=https://github.com/mozilla/sccache
license=(Apache)
depends=(openssl)
makedepends=(cargo)
checkdepends=(openssl-1.0)
source=(sccache-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha512sums=('1f7495aa7c0749c4bfbd85a88a304a6ed18cc9bfcd341f0f1a668a743ae31d355bc8c5b3199b048d8bcab3ce8e9c8b844a609e4c3009d4e5497dd080aa881a45')

prepare() {
  # Lifetime annotation is required for the version-compare crate with Rust 1.40
  # Upgrade it to 0.0.9 which added the annotation
  sed -r "s@(version-compare = \{ version = \")(.*)(\".*)@\10.0.9\3@" \
    -i sccache-$pkgver/Cargo.toml
}

build() {
  cd sccache-$pkgver
  # sccache-dist is only supported on x86_64
  cargo build \
    $([ $CARCH = aarch64 ] && echo --features=all || echo --all-features) \
    --release
}

check() {
  # Tests require sccache-dist. Disable for now.
  [ $CARCH = aarch64 ] && return

  cd sccache-$pkgver

  # Older native-tls crate depends on older openssl crate
  OPENSSL_LIB_DIR=/usr/lib/openssl-1.0 \
    OPENSSL_INCLUDE_DIR=/usr/include/openssl-1.0 \
    cargo test --release
}

package() {
  cd sccache-$pkgver
  install -D target/release/sccache -t "$pkgdir"/usr/bin
  install -Dm 644 README.md -t "$pkgdir"/usr/share/doc/sccache
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/sccache
}
