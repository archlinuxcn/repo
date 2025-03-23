# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.50.0
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
sha256sums_x86_64=('1e4b9e1814ff0542c8d6cc6a16884098dcbdc7bc8e6007156b35e879015d7b79')
sha256sums_aarch64=('b6ed742e27e0c4f8b9f9256d1433e8e98e584233874b2c86ddb4ddfd3de8a727')
sha256sums_i686=('898123e70f8cf76682862cc45d8f965a413be8e4199f85b28eec8a394de90bb4')
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
