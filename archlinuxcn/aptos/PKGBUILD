# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=aptos
pkgver=7.2.0
pkgrel=1
pkgdesc='Aptos is a layer 1 blockchain built to support the widespread use of blockchain through better technology and user experience.'
url='https://aptos.dev'
arch=(x86_64)
license=(Apache-2.0)
depends=(gcc-libs glibc libelf libssl.so libcrypto.so systemd-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/aptos-labs/aptos-core#tag=aptos-cli-v$pkgver)
sha512sums=('2180d1f10d33faa1389a5219b708bb0b218839ed7467fd1a6ce0eb64c46ef86c5f176fee43f19d927444e505bfd574152bfca20c4f2f1311049feeb87532809a')
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
