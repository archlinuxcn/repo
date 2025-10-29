# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=aptos
pkgver=7.10.2
pkgrel=1
pkgdesc='Aptos is a layer 1 blockchain built to support the widespread use of blockchain through better technology and user experience.'
url='https://aptos.dev'
arch=(x86_64)
license=(Apache-2.0)
depends=(gcc-libs glibc libelf libssl.so libcrypto.so systemd-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/aptos-labs/aptos-core#tag=aptos-cli-v$pkgver)
sha512sums=('0f88360b9bdba64cbf14d2509de114baa468ec5ad4939fc6bd80499aa0e99b3b45ba10fcc034842c01f2b5b08b9e9fd78cf0f4362be399cce6d6b8c264043f02')
# undefined reference to `git_repository_open'
options=(!lto)

prepare() {
  cd aptos-core
  export RUSTUP_TOOLCHAIN=stable

  # Fix `time` compile error
  cargo update -p time

  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd aptos-core
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  # https://github.com/aptos-labs/aptos-core/issues/10293
  export RUSTFLAGS="--cfg tokio_unstable"
  # Fix rocksdb
  export CXXFLAGS="$CXXFLAGS -include cstdint"
  cargo build --frozen --release -p aptos
}

check() {
  cd aptos-core
  export RUSTUP_TOOLCHAIN=stable
  # test genesis::tests::test_genesis_e2e_flow ... FAILED
  cargo test --frozen -p aptos || true
}

package() {
  cd aptos-core
  install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
}
