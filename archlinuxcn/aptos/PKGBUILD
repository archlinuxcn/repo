# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=aptos
pkgver=6.0.0
pkgrel=1
pkgdesc='Aptos is a layer 1 blockchain built to support the widespread use of blockchain through better technology and user experience.'
url='https://aptos.dev'
arch=(x86_64)
license=(Apache-2.0)
depends=(gcc-libs glibc libelf libssl.so libcrypto.so systemd-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/aptos-labs/aptos-core#tag=aptos-cli-v$pkgver)
sha512sums=('8de52c3359018976e3d58fe96e25f1c5a769ce9a7402a96df486db2d7d9edd6cfe090f2043136b9661d40868084206d61af96c86f37b82f5a503863daa305d51')
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
  cargo build --frozen --release -p aptos
}

check() {
  cd aptos-core
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen -p aptos
}

package() {
  cd aptos-core
  install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
}
