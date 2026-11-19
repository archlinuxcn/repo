# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=sui
pkgver=1.84.1
pkgrel=1
pkgdesc='Sui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language.'
url='https://sui.io'
arch=(x86_64)
license=(Apache-2.0)
depends=(glibc libgcc libstdc++)
makedepends=(git cargo clang)
source=(git+https://github.com/MystenLabs/$pkgname#tag=mainnet-v$pkgver)
sha512sums=('ee060ffdc8ef5dc663408a03eac0ca63b1e6f35565435f26f985dc6b7bda9c301c872425cf57912e2c22770b1f8ce4178baf488d0def63d7203bc6484906287b')
# https://github.com/briansmith/ring/issues/1444
options=(!lto)

prepare() {
  cd $pkgname
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd $pkgname
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target

  # Fix rocksdb
  export CXXFLAGS="$CXXFLAGS -include cstdint"

  binarys=(
    move-analyzer
    # sui
    sui-bridge
    sui-bridge-cli
    sui-faucet
    sui-node
    sui-test-validator
    sui-tool
  )
  for binary in "${binarys[@]}"; do
    cargo build --frozen --release -p $binary
  done

  # Suggested by https://docs.sui.io/guides/developer/getting-started/sui-install#install-sui-binaries-from-source
  cargo build --frozen --release -p sui --features tracing
}

package() {
  cd $pkgname

  binarys=(sui sui-bridge sui-bridge-cli sui-faucet sui-node sui-test-validator sui-tool)
  for binary in "${binarys[@]}"; do
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$binary"
  done
}
