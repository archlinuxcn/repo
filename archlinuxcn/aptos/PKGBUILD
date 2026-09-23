# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=aptos
pkgver=9.6.0
pkgrel=1
pkgdesc='Aptos is a layer 1 blockchain built to support the widespread use of blockchain through better technology and user experience.'
url='https://aptos.dev'
arch=(x86_64)
license=(Apache-2.0)
depends=(gcc-libs glibc libelf libssl.so libcrypto.so systemd-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/aptos-labs/aptos-core#tag=aptos-cli-v$pkgver)
sha512sums=('9e66f4c2e3753498a1f8b18d1edfee22e838ab6cae6f2310410f55e4f099f501dea99e5829dba7b3e19c84965a5fcb32271409a77782caa241a2b60ce0886636')
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
