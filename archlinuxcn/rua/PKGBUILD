# Maintainer: Vasili Novikov (replace "vvv" with "v" in email) vvvasya.novikov+cm3513git@gmail.com
pkgname=rua
pkgver=0.19.8
pkgrel=1
pkgdesc='AUR helper in Rust providing control, review, patch application and safe build options'
url='https://github.com/vn971/rua'
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/vn971/rua/archive/v${pkgver}.tar.gz")
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
license=('GPL3')

makedepends=('cargo' 'libseccomp')
depends=('bubblewrap' 'git' 'pacman' 'xz')
optdepends=(
  'bubblewrap-suid: version of bubblewrap that works on linux-hardened kernel'
  'shellcheck: allows checking PKGBUILD scripts, taking care of special variables'
  'sudo: allows package installation via sudo, if desired'
)

# Depending on the environment Rust packages may fail to build with LTO,
# see https://aur.archlinux.org/packages/rua#comment-861014
options=('!lto')

b2sums=(bc3f5c75f6953a01b30403924a4af57502b2be19a28d7b17f5453ee7de47ff4e58b492cf0ae03c5cd99547524a8715498f46378b3e7236f6fd6ffcb71e4eb387)

#options+=(!strip)  # uncomment if you want readable stack traces

prepare() {
  cd "$srcdir/$pkgname-$pkgver"
  cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build () {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p target/completions

  # RUSTUP_TOOLCHAIN is specified in project's .rust-toolchain.toml
  COMPLETIONS_DIR=target/completions \
    CARGO_TARGET_DIR=target \
    cargo build --frozen --release
}

check() {
  cd "$srcdir/$pkgname-$pkgver"
  cargo test --frozen
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm0755 target/release/rua "${pkgdir}/usr/bin/rua"

  install -Dm0644 target/completions/rua.bash "${pkgdir}/usr/share/bash-completion/completions/rua.bash"
  install -Dm0644 target/completions/rua.fish "${pkgdir}/usr/share/fish/completions/rua.fish"
  install -Dm0644 target/completions/_rua "${pkgdir}/usr/share/zsh/functions/Completion/Linux/_rua"
}
