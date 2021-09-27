# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.17.1
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
sha256sums_x86_64=('2824687fe3965374f463ae49f9d8abd9d3d556a0f63880bc78b5ee02098ba142')
sha256sums_aarch64=('d14539dbbbb2269b6c3e105b83fa7dac744c1cfaf39f7eb2760293fec856e738')
sha256sums_armv7h=('2b1e63cbd62cce1a15c7cf0635f85b6bc7de880563cdf4b3a20422c9c30a616c')
sha256sums_i686=('04ec4ffd8fab1931e53f70beb3497770b42f4d37d7469c1973a0eeeccd5e8989')
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
