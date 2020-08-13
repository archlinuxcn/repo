# Maintainer: Vasia Novikov <n1dr+cmarchlinux@yaaandex.com> (replace "aaa" with "a")
pkgname=rua
pkgver=0.17.12
pkgrel=1
pkgdesc='AUR helper in Rust providing control, review, patch application and safe build options'
url='https://github.com/vn971/rua'
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/vn971/rua/archive/v${pkgver}.tar.gz")
arch=('x86_64' 'i686')
license=('GPL3')

makedepends=('cargo')
depends=('bubblewrap' 'git' 'pacman' 'xz')
optdepends=(
  'bubblewrap-suid: version of bubblewrap that works on linux-hardened kernel'
  'shellcheck: check PKGBUILD scripts, taking care of special variables'
  'sudo: package installation can be done via sudo, if convenient'
)

#options+=(!strip)  # uncomment if you want readable stack traces

sha256sums=(f98cd563b5b90463e2f72b2915bfc4f9da79825d6ccd0cf16e62aa9a7fa6a6d3)

build () {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p target/completions

  if pacman -T pacman-git > /dev/null; then
    _features="git"
  fi

  RUSTUP_TOOLCHAIN=stable \
    COMPLETIONS_DIR=target/completions \
    cargo build --features "${_features:-}" --release
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 target/release/rua "${pkgdir}/usr/bin/rua"

  install -Dm644 target/completions/rua.bash "${pkgdir}/usr/share/bash-completion/completions/rua.bash"
  install -Dm644 target/completions/rua.fish "${pkgdir}/usr/share/fish/completions/rua.fish"
  install -Dm644 target/completions/_rua "${pkgdir}/usr/share/zsh/functions/Completion/Linux/_rua"
}

