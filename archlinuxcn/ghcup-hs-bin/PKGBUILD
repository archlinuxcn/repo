# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.14
pkgrel=1
pkgdesc="an installer for the general purpose language Haskell"
arch=('x86_64')
url="https://gitlab.haskell.org/haskell/ghcup-hs"
license=('LGPL3')
depends=()
optdepends=('curl'
            'wget'
            "ncurses5-compat-libs: using older ghc's linking against libtinfo.so.5")
conflicts=('ghcup-git')
source=(ghcup-$pkgver::https://downloads.haskell.org/~ghcup/$pkgver/x86_64-linux-ghcup-$pkgver
        ghcup-comp-bash-$pkgver::$url/-/raw/v$pkgver/shell-completions/bash
        ghcup-comp-zsh-$pkgver::$url/-/raw/v$pkgver/shell-completions/zsh
        ghcup-comp-fish-$pkgver::$url/-/raw/v$pkgver/shell-completions/fish)
sha256sums=('e9b314d248f4d4604ce64cee1be7161c77c8940efd11986c9205779ec3b598dd'
            '2cfbd028499615507bb081b4f6668caa34fe700ed5a4895f8c3716a54e53cafc'
            '3b2f4a9df87c17f3f6472cda80eca8357485a9efd78f32223559f797d55d0d31'
            '0b3afa4d80de4afcc89779911b6c64e319c55aef185dff2843e6d410a530bb3f')
install="$pkgname.install"

package() {
  install -Dm755 ghcup-$pkgver "$pkgdir/usr/bin/ghcup"
  install -Dm644 ghcup-comp-bash-$pkgver "$pkgdir/usr/share/bash-completion/completions/ghcup"
  install -Dm644 ghcup-comp-zsh-$pkgver "$pkgdir/usr/share/zsh/site-functions/_ghcup"
  install -Dm644 ghcup-comp-fish-$pkgver "$pkgdir/usr/share/fish/vendor_completions.d/ghcup.fish"
}
