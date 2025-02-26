# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=sui
pkgver=1.43.1
pkgrel=1
pkgdesc='Sui, a next-generation smart contract platform with high throughput, low latency, and an asset-oriented programming model powered by the Move programming language.'
url='https://sui.io'
arch=(x86_64)
license=(Apache-2.0)
depends=(glibc gcc-libs)
makedepends=(git cargo clang)
source=(git+https://github.com/MystenLabs/$pkgname#tag=mainnet-v$pkgver)
sha512sums=('f0312019ec6b80ac05dacaa6a5075b4d5bceea7228bb494b79754a307389b13b6047645d30348d05b70682e84e24fed3ce6e56476c940cf342e8aa265fad83b5')
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

  binarys=(move-analyzer sui sui-bridge sui-bridge-cli sui-data-ingestion sui-faucet sui-graphql-rpc sui-node sui-test-validator sui-tool)
  for binary in "${binarys[@]}"; do
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$binary"
  done
}
