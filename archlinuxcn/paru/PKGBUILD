# Maintainer: Morgan <morganamilo@archlinux.org>
pkgname=paru
pkgver=0.99.3
pkgrel=1
pkgdesc='AUR helper based on yay'
url='https://github.com/morganamilo/paru'
source=("$pkgname-$pkgver::https://github.com/Morganamilo/paru/archive/v$pkgver.tar.gz")
backup=("etc/paru.conf")
arch=('x86_64' 'i686')
license=('GPL3')

makedepends=('cargo')
depends=('git' 'pacman')
optdepends=('asp: downloading repo pkgbuilds')

sha256sums=('3b2e1dd2f877bc53165675ad8516203962c094324410e022e21d9ffe542bd6af')

build () {
  cd "$srcdir/$pkgname-$pkgver"

  if pacman -T pacman-git > /dev/null; then
    _features+="git,generate,"
  fi

  if [[ $(rustc -V) == *"nightly"* ]]; then
    _features+="backtrace,"
  fi

  cargo build --features "${_features:-}" --release
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  install -Dm755 target/release/paru "${pkgdir}/usr/bin/paru"
  install -Dm644 paru.conf "${pkgdir}/etc/paru.conf"

  install -Dm644 man/paru.8 "$pkgdir/usr/share/man/man8/paru.8"
  install -Dm644 man/paru.conf.5 "$pkgdir/usr/share/man/man5/paru.conf.5"

  install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/paru.bash"
  install -Dm644 completions/fish "${pkgdir}/usr/share/fish/completions/paru.fish"
  install -Dm644 completions/zsh "${pkgdir}/usr/share/zsh/functions/Completion/Linux/_paru"
}
