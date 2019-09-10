# Maintainer: Vasia Novikov <n1dr+cmarchlinux@yaaandex.com> (replace "aaa" with "a")
pkgname=rua
pkgver=0.14.12
pkgrel=1
pkgdesc='AUR helper in Rust providing control, review and jailed/offline build options'
url='https://github.com/vn971/rua'
source=("https://github.com/vn971/rua/archive/${pkgver}.tar.gz")
arch=('x86_64' 'i686')
license=('GPL3')

makedepends=('cargo')
depends=('bubblewrap' 'git' 'pacman' 'xz' 'openssl')
optdepends=(
  'bubblewrap-suid: version of bubblewrap that works on linux-hardened kernel'
  'sudo: package installation can be done via sudo, if convenient'
)

#options+=(!strip)  # uncomment if you want readable stack traces

sha256sums=(a290b251820d673be86563deafe38c5ad0c7760b14b10dbbffce70c9d11d7382)

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

