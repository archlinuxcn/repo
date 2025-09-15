# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: Ivan Marquesi Lerner <ivanmlerner@protonmail.com>
# Contributor: BlackCatDevel0per

pkgname=solana  
epoch=1
pkgver=2.3.9
# https://github.com/anza-xyz/agave/blob/v$pkgver/scripts/spl-token-cli-version.sh
_splTokenCliVersion=4.1.1
pkgrel=1
pkgdesc="A fast, secure, and censorship resistant blockchain."
url="https://www.solana.com"
arch=(x86_64)
license=(Apache-2.0)
depends=(bash bzip2 cargo gcc-libs glibc systemd-libs)
makedepends=(git protobuf clang llvm)
provides=(spl-token)
source=(git+https://github.com/anza-xyz/agave.git#tag=v$pkgver
        git+https://github.com/solana-labs/solana-program-library.git#tag=token-cli-v$_splTokenCliVersion
        $pkgname.sysusers
        $pkgname.tmpfiles
        $pkgname-sbf_sdk-path.patch)
sha256sums=('4662dedbd518f3642a9d9cdf73be297311def3ed89c68a2b06a14e1af3f95a78'
            'd0d7c7e98b42a6613d4ba1ddc8ec7650434793bab5925bf565de6cf3ba6093a1'
            'bf7e015436e3d15e70fc67f323bbd04163f79a4de7d06a254a5409bd031227b0'
            'a0f9ee2a24ab97da977eed1dd68a92165c2f2e6d5467462fe83c762031f4e02b'
            '8fee0981fb31343719c6f4f3b845dd8d957ad7d38319c0cc80f4637f9210874c')
install=$pkgname.install
options=(!lto)

# https://github.com/anza-xyz/agave/blob/v$pkgver/scripts/cargo-install-all.sh
_BINS=(
  solana
  solana-faucet
  solana-genesis
  solana-gossip
  agave-install
  solana-keygen
  solana-log-analyzer
  solana-net-shaper
  agave-validator
  rbpf-cli
  cargo-build-sbf
  cargo-test-sbf
  agave-install-init
  solana-stake-accounts
  solana-test-validator
  solana-tokens
  agave-watchtower
)

_DCOU_BINS=(
  agave-ledger-tool
  solana-bench-tps
  solana-dos
)

# https://github.com/anza-xyz/agave/blob/v$pkgver/scripts/dcou-tainted-packages.sh
_dcou_tainted_packages=(
  solana-accounts-bench
  solana-banking-bench
  agave-ledger-tool
  solana-bench-tps
  agave-store-tool
  agave-store-histogram
  agave-accounts-hash-cache-tool
  solana-dos
)

prepare() {
  export RUSTUP_TOOLCHAIN=stable
  cd $srcdir/agave
  patch -Np1 -i ../$pkgname-sbf_sdk-path.patch
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"

  cd $srcdir/solana-program-library
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cd $srcdir/agave

  # error: hiding a lifetime that's elided elsewhere is confusing
  sed -i '/^\[workspace\.lints\.rust\]$/,+1d' Cargo.toml

  local binargs=()
  for bin in "${_BINS[@]}"; do
    binargs+=(--bin "$bin")
  done

  local excludeArgs=()
  for package in "${_dcou_tainted_packages[@]}"; do
    excludeArgs+=(--exclude "$package")
  done

  local dcouBinArgs=()
  for bin in "${_DCOU_BINS[@]}"; do
    dcouBinArgs+=(--bin "$bin")
  done

  # Fix rocksdb
  export CXXFLAGS="$CXXFLAGS -include cstdint"

  cargo build --frozen --release "${binargs[@]}" --workspace "${excludeArgs[@]}"
  cargo build --frozen --release "${dcouBinArgs[@]}"
  cargo build --frozen --release --manifest-path programs/bpf_loader/gen-syscall-list/Cargo.toml
  cargo run --frozen --release --bin gen-headers

  cd $srcdir/solana-program-library
  cargo build --frozen --release --bin spl-token
}

package() {
  cd $srcdir/agave
  for bin in "${_BINS[@]}"; do
    install -Dm755 target/release/$bin -t $pkgdir/usr/bin
  done
  for bin in "${_DCOU_BINS[@]}"; do
    install -Dm755 target/release/$bin -t $pkgdir/usr/bin
  done

  install -dm755 $pkgdir/usr/lib/$pkgname/platform-tools-sdk
  cp -a platform-tools-sdk/sbf $pkgdir/usr/lib/$pkgname/platform-tools-sdk

  cd $srcdir/solana-program-library
  install -Dm755 target/release/spl-token -t $pkgdir/usr/bin

  install -Dm644 $srcdir/$pkgname.sysusers $pkgdir/usr/lib/sysusers.d/$pkgname.conf
  install -Dm644 $srcdir/$pkgname.tmpfiles $pkgdir/usr/lib/tmpfiles.d/$pkgname.conf
}
