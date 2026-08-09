# Maintainer: Rubin Simons <me@rubin55.org>
# Contributor: amesgen <amesgen AT amesgen DOT de>

pkgname=ghcup-hs-bin
pkgver=0.2.6.2
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
sha256sums_x86_64=('9ed5da5449b48043a0d17e767c05d2ef585e25a639bb934329496c6d2fad9cf8')
sha256sums_aarch64=('65a5f05120288ee4f1a81d28825374b6af317456a351a586adfce90c6dc29e3b')
sha256sums_i686=('6032f7461760641da4be32f3415b4deda39ba8e1cfa8622aacfb01d177ef1a29')
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
