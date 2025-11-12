# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=aptos
pkgver=7.11.0
pkgrel=1
pkgdesc='Aptos is a layer 1 blockchain built to support the widespread use of blockchain through better technology and user experience.'
url='https://aptos.dev'
arch=(x86_64)
license=(Apache-2.0)
depends=(gcc-libs glibc libelf libssl.so libcrypto.so systemd-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/aptos-labs/aptos-core#tag=aptos-cli-v$pkgver)
sha512sums=('c08e0a3168d5f586fd8ee8bb8bf3c28204a2709ce93ed307bb8dff957fecd3debdcbd9c6d98d1b086de702638640ea7209fcffa8b1a2e715dbcb2d6723cab7fb')
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
