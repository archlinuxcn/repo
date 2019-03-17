# Maintainer: Vasia Novikov <n1dr+cmarchlinux@yaaandex.com> (replace "aaa" with "a")

pkgname=rua
pkgver=0.13.0
pkgrel=1
pkgdesc='secure jailed AUR helper in rust'
url='https://github.com/vn971/rua'
source=("https://github.com/vn971/rua/archive/${pkgver}.tar.gz")
arch=('x86_64' 'i686')
license=('GPL3')
makedepends=('cargo')
depends=('bubblewrap' 'git')

#options+=(!strip)  # uncomment to have readable stack traces

sha256sums=(435b9f44267bf1c67c9c4d36d0cbc043b5674b98415cdb7c1dc0385ef16bd36e)

build () {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p target/completions
  RUSTUP_TOOLCHAIN=stable \
    COMPLETIONS_DIR=target/completions \
    cargo build --release
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 target/release/rua "${pkgdir}/usr/bin/rua"

  install -Dm644 target/completions/rua.bash "${pkgdir}/usr/share/bash-completion/completions/rua.bash"
  install -Dm644 target/completions/rua.fish "${pkgdir}/usr/share/fish/completions/rua.fish"
  install -Dm644 target/completions/_rua "${pkgdir}/usr/share/zsh/functions/Completion/Linux/_rua"
}
