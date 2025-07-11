# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=sui
pkgver=1.51.5
pkgrel=1
pkgdesc='Sui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language.'
url='https://sui.io'
arch=(x86_64)
license=(Apache-2.0)
depends=(glibc gcc-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/MystenLabs/$pkgname#tag=mainnet-v$pkgver)
sha512sums=('af529b8ecf0ccc8665a93247a6735f67527e6d90b97d5cb19ea349d2145d08b0dc660ac442482a784b0f340f9af5cddb08c56fa216199891d325632319b9d004')
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
    sui-data-ingestion
    sui-faucet
    sui-graphql-rpc
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

  binarys=(sui sui-bridge sui-bridge-cli sui-data-ingestion sui-faucet sui-graphql-rpc sui-node sui-test-validator sui-tool)
  for binary in "${binarys[@]}"; do
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$binary"
  done
}
