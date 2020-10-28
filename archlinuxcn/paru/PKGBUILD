# Maintainer: Morgan <morganamilo@archlinux.org>
pkgname=paru
pkgver=1.0.0
pkgrel=1
pkgdesc='AUR helper based on yay'
url='https://github.com/morganamilo/paru'
source=("$pkgname-$pkgver::https://github.com/Morganamilo/paru/archive/v$pkgver.tar.gz")
backup=("etc/paru.conf")
arch=('x86_64' 'i686')
license=('GPL3')
makedepends=('cargo')
depends=('git' 'pacman')
optdepends=('asp: downloading repo pkgbuilds' 'bat: colored pkgbuild printing')
sha256sums=('11ca7e63fe9c6bbdf89bafe4fc19e13e08120fb136bbedac91a594777d769bbc')

build () {
  cd "$srcdir/$pkgname-$pkgver"

  if pacman -T pacman-git > /dev/null; then
    _features+="git,generate,"
  fi

  if [[ $(rustc -V) == *"nightly"* ]]; then
    _features+="backtrace,"
  fi

  cargo build --locked --features "${_features:-}" --release
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
