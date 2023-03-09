# Maintainer: Vasili Novikov (replace "nnn" with "n" in email) <nnn1dr+cmarchlinux@yandex.com>
pkgname=rua
pkgver=0.19.4
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

b2sums=(be2705b2b47e40757605ad80dddff397f5f584c69b677dfea15ad8fa5dea3f48673af02d72ea4b2fe2ce2b86cb035f48470f2c9bd458af44d38ad370dafd4031)

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
