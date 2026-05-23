# Maintainer: DeepChirp <deepchirp@archlinuxcn.org>
# Contributor: bbaa <bbaa@bbaa.moe>
# Contributor: cap153 <1536989047@qq.com>

_pkgname=EasyTier
pkgbase=easytier
pkgname=($pkgbase $pkgbase-core $pkgbase-cli $pkgbase-web)
pkgver=2.6.4
pkgrel=4
pkgdesc="A simple, decentralized mesh VPN with WireGuard support."
arch=('x86_64' 'aarch64' 'armv7h' 'loongarch64' 'riscv64' 'mipsel' 'mips64el')
url="https://github.com/EasyTier/EasyTier"
license=('LGPL-3.0-only')
depends=('glibc' 'libgcc' 'zstd')
makedepends=('cargo' 'protobuf' 'rust-bindgen' 'clang' 'llvm' 'lld' 'sqlite'
             'nodejs' 'pnpm') # for embeded web
source=(
    "$_pkgname-$pkgver.tar.gz::https://github.com/EasyTier/EasyTier/archive/refs/tags/v$pkgver.tar.gz"
    "easytier.service"
    "config.toml")
sha256sums=('352c0866da709415a837405a6ce4f51b8dfae27e5d5c1da1fb4d8f7338e46795'
            'c3a88a02c96ccbed58908d91da89338c2d093ec3e571f3861c36a5cd0a92bb21'
            '05518beea8b047d5e9b9adb14f26f85a91e4eea81ead7eeb4743f8978e1fd842')

prepare() {
    cd "$_pkgname-$pkgver"

    export PNPM_HOME="$srcdir/.pnpm-home"
    export npm_config_store_dir="$srcdir/.pnpm-store"
    pnpm -r install --frozen-lockfile

    export RUSTUP_TOOLCHAIN=stable

    cargo fetch --locked --target host-tuple
}

build() {
    cd "$_pkgname-$pkgver"

    export PNPM_HOME="$srcdir/.pnpm-home"
    export npm_config_store_dir="$srcdir/.pnpm-store"
    pnpm -r --filter "./easytier-web/*" build

    # https://github.com/briansmith/ring/issues/1444#issuecomment-1763272308
    # So we use Clang instead of GCC.
    export CC="$(command -v clang)"
    export AR="$(command -v llvm-ar)"
    export NM="$(command -v llvm-nm)"
    export RANLIB="$(command -v llvm-ranlib)"
    _LD_LLD="$(command -v ld.lld)"

    export RUSTFLAGS="-Clinker=$CC -Clink-arg=-fuse-ld=${_LD_LLD}"
    export RUSTDOCFLAGS="$RUSTFLAGS"

    export CARGO_PROFILE_RELEASE_LTO=true
    export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1

    # Used for dynamic linking
    export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
    export ZSTD_SYS_USE_PKG_CONFIG=1

    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target

    cargo build --frozen --release --features=embed

    install -d completions

    ./target/release/easytier-core --gen-autocomplete bash   > completions/core-bash
    ./target/release/easytier-core --gen-autocomplete fish   > completions/core-fish
    ./target/release/easytier-core --gen-autocomplete zsh    > completions/core-zsh
    ./target/release/easytier-core --gen-autocomplete nu     > completions/core-nu
    ./target/release/easytier-core --gen-autocomplete elvish > completions/core-elvish

    ./target/release/easytier-cli    gen-autocomplete bash   > completions/cli-bash
    ./target/release/easytier-cli    gen-autocomplete fish   > completions/cli-fish
    ./target/release/easytier-cli    gen-autocomplete zsh    > completions/cli-zsh
    ./target/release/easytier-cli    gen-autocomplete nu     > completions/cli-nu
    ./target/release/easytier-cli    gen-autocomplete elvish > completions/cli-elvish
}

package_easytier() {
    pkgdesc="A simple, decentralized mesh VPN with WireGuard support."
    depends=('easytier-core' 'easytier-cli' 'easytier-web')
}

package_easytier-core() {
    backup=('etc/easytier/config.toml')

    install -dm755 "$pkgdir/var/lib/easytier"
    install -Dm644 "easytier.service" "$pkgdir/usr/lib/systemd/system/easytier.service"
    install -Dm644 "config.toml" "$pkgdir/etc/easytier/config.toml"

    cd "$_pkgname-$pkgver"
    install -Dm755 "target/release/easytier-core" -t "$pkgdir/usr/bin"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/easytier/LICENSE"

    install -Dm644 completions/core-bash   "$pkgdir/usr/share/bash-completion/completions/$pkgname"
    install -Dm644 completions/core-fish   "$pkgdir/usr/share/fish/vendor_completions.d/$pkgname.fish"
    install -Dm644 completions/core-zsh    "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
    install -Dm644 completions/core-nu     "$pkgdir/usr/share/nushell/vendor/autoload/$pkgname.nu"
    install -Dm644 completions/core-elvish "$pkgdir/usr/share/elvish/lib/$pkgname.elv"
}

package_easytier-cli() {
    cd "$_pkgname-$pkgver"
    install -Dm755 "target/release/easytier-cli" -t "$pkgdir/usr/bin"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/easytier/LICENSE-cli"

    install -Dm644 completions/cli-bash   "$pkgdir/usr/share/bash-completion/completions/$pkgname"
    install -Dm644 completions/cli-fish   "$pkgdir/usr/share/fish/vendor_completions.d/$pkgname.fish"
    install -Dm644 completions/cli-zsh    "$pkgdir/usr/share/zsh/site-functions/_$pkgname"
    install -Dm644 completions/cli-nu     "$pkgdir/usr/share/nushell/vendor/autoload/$pkgname.nu"
    install -Dm644 completions/cli-elvish "$pkgdir/usr/share/elvish/lib/$pkgname.elv"
}

package_easytier-web() {
    depends+=('sqlite')
    cd "$_pkgname-$pkgver"
    install -Dm755 "target/release/easytier-web" -t "$pkgdir/usr/bin"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/easytier/LICENSE-web"
}
