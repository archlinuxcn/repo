# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.17
pkgrel=1
pkgdesc="an installer for the general purpose language Haskell"
arch=('x86_64' 'aarch64' 'armv7h' 'i686')
url="https://gitlab.haskell.org/haskell/ghcup-hs"
license=('LGPL3')
depends=()
optdepends=('curl'
            'wget'
            "ncurses5-compat-libs: using older ghc's linking against libtinfo.so.5")
conflicts=('ghcup-git')
source_x86_64=(ghcup-$pkgver-x86_64::https://downloads.haskell.org/~ghcup/$pkgver/x86_64-linux-ghcup-$pkgver)
source_aarch64=(ghcup-$pkgver-aarch64::https://downloads.haskell.org/~ghcup/$pkgver/aarch64-linux-ghcup-$pkgver)
source_armv7h=(ghcup-$pkgver-armv7h::https://downloads.haskell.org/~ghcup/$pkgver/armv7-linux-ghcup-$pkgver)
source_i686=(ghcup-$pkgver-i686::https://downloads.haskell.org/~ghcup/$pkgver/i386-linux-ghcup-$pkgver)
sha256sums_x86_64=('1eaa33af4180f97edf02822d6d711ce618d9828fe9ebbf042d198fe6c1c9d153')
sha256sums_aarch64=('be67cf8800ae305c5ba210b645f4fce8751763f3eac3db399f6efca145b7ab38')
sha256sums_armv7h=('fe54ded2fafff4f8d82e511229f257f4c3b87b14c796f9b5b0ea35c359c26cb0')
sha256sums_i686=('d0f887b13a2c7a11477dc54cb90b446ef0ebe1d2a6bfbf60ccd4b37fc5de70cc')
install="$pkgname.install"

package() {
  install -Dm755 ghcup-$pkgver-$CARCH "$pkgdir/usr/bin/ghcup"
  _install_completion_script bash bash-completion/completions/ghcup
  _install_completion_script zsh zsh/site-functions/_ghcup
  _install_completion_script fish fish/vendor_completions.d/ghcup.fish
}

_install_completion_script() {
  install -Dm644 <("$pkgdir/usr/bin/ghcup" --$1-completion-script "/usr/bin/ghcup") "$pkgdir/usr/share/$2"
}
