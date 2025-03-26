# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.50.1
pkgrel=1
pkgdesc="an installer for the general purpose language Haskell"
arch=('x86_64' 'aarch64' 'i686')
url="https://www.haskell.org/ghcup/"
license=('LGPL3')
depends=()
optdepends=('curl'
            'wget'
            "ncurses5-compat-libs: using older ghc's linking against libtinfo.so.5")
provides=('ghcup-hs')
conflicts=('ghcup-hs')
source_x86_64=(ghcup-$pkgver-$pkgrel-x86_64::https://downloads.haskell.org/~ghcup/$pkgver/x86_64-linux-ghcup-$pkgver)
source_aarch64=(ghcup-$pkgver-$pkgrel-aarch64::https://downloads.haskell.org/~ghcup/$pkgver/aarch64-linux-ghcup-$pkgver)
source_i686=(ghcup-$pkgver-$pkgrel-i686::https://downloads.haskell.org/~ghcup/$pkgver/i386-linux-ghcup-$pkgver)
sha256sums_x86_64=('b3486feede578fecb04275a45d8187088c3fdc596d6f40aab214c215eabdb223')
sha256sums_aarch64=('877a1b66b94d00235e4d645c6fe0de26c0661a0b897cc4d2a2cf98fba74afe65')
sha256sums_i686=('c266ee62acb85091acbbe6a05f588ef05f8275279f98aa0c6deea26cbff86aa0')
install="$pkgname.install"

package() {
  install -Dm755 ghcup-$pkgver-$pkgrel-$CARCH "$pkgdir/usr/bin/ghcup"
  _install_completion_script bash bash-completion/completions/ghcup
  _install_completion_script zsh zsh/site-functions/_ghcup
  _install_completion_script fish fish/vendor_completions.d/ghcup.fish
}

_install_completion_script() {
  install -Dm644 <("$pkgdir/usr/bin/ghcup" --$1-completion-script "/usr/bin/ghcup") "$pkgdir/usr/share/$2"
}
