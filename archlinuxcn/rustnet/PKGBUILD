# Maintainer: DeepChirp <DeepChirp@outlook.com>
# Maintainer: lilydjwg <lilydjwg@gmail.com>

pkgname=rustnet
_pkgname=${pkgname%}
_reponame=${pkgname%}
pkgver=0.14.0
pkgrel=1
pkgdesc="Real-time network monitoring TUI with process identification via eBPF and deep packet inspection"
arch=('x86_64' 'armv7h' 'aarch64')
_author=domcyrus
url="https://github.com/${_author}/${_reponame}"
license=('Apache-2.0')
depends=('libpcap' 'libelf' 'zlib' 'gcc-libs' 'glibc')
makedepends=('git' 'cargo' 'pkgconf' 'clang' 'llvm' 'lld' 'libbpf')
provides=(${pkgname%})
conflicts=("${pkgname%}-git" "${pkgname%}-bin")
install=$_pkgname.install
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "rustnet-setcap.hook")
sha256sums=('92c252523ab9c7ab6b2f844aab995d8ef11a6140039c003dd68a58ddd2ef3372'
            'b14ba212f2a589ca327a2e59563a4fdd3787c022baf43b6dc249b03814757cc4')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"

    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
    cd "$srcdir/$pkgname-$pkgver"

    export RUSTUP_TOOLCHAIN=stable

    # https://github.com/briansmith/ring/issues/1444#issuecomment-1763272308
    # So we use Clang instead of GCC.
    export CC="$(command -v clang)"
    export AR="$(command -v llvm-ar)"
    export NM="$(command -v llvm-nm)"
    export RANLIB="$(command -v llvm-ranlib)"
    _LD_LLD="$(command -v ld.lld)"

    export RUSTFLAGS="-Clinker=$CC -Clink-arg=-fuse-ld=${_LD_LLD}"
    export RUSTDOCFLAGS="$RUSTFLAGS"

    export CARGO_PROFILE_RELEASE_LTO=thin
    export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
    # Use ebpf for better performance
    CFLAGS='-flto=auto' cargo build --frozen --release --features ebpf
}

check() {
    cd "$srcdir/$pkgname-$pkgver"

    export RUSTUP_TOOLCHAIN=stable
    export CC="$(command -v clang)"
    export AR="$(command -v llvm-ar)"
    export NM="$(command -v llvm-nm)"
    export RANLIB="$(command -v llvm-ranlib)"
    _LD_LLD="$(command -v ld.lld)"

    export RUSTFLAGS="-Clinker=$CC -Clink-arg=-fuse-ld=${_LD_LLD}"
    export RUSTDOCFLAGS="$RUSTFLAGS"

    export CARGO_PROFILE_RELEASE_LTO=thin
    export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
    CFLAGS='-flto=auto' cargo test --frozen --release --features ebpf
}

package() {
    cd "$srcdir/$pkgname-$pkgver"

    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$_pkgname"
    install -Dm644 -t "$pkgdir/usr/share/$_pkgname/hooks/" "$srcdir/rustnet-setcap.hook"
}
