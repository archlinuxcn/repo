# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.40.0
pkgrel=1
pkgdesc="an installer for the general purpose language Haskell"
arch=('x86_64' 'aarch64' 'armv7h' 'i686')
url="https://www.haskell.org/ghcup/"
license=('LGPL3')
depends=()
optdepends=('curl'
            'wget'
            "ncurses5-compat-libs: using older ghc's linking against libtinfo.so.5")
conflicts=('ghcup-git')
source_x86_64=(ghcup-$pkgver-$pkgrel-x86_64::https://downloads.haskell.org/~ghcup/$pkgver/x86_64-linux-ghcup-$pkgver)
source_aarch64=(ghcup-$pkgver-$pkgrel-aarch64::https://downloads.haskell.org/~ghcup/$pkgver/aarch64-linux-ghcup-$pkgver)
source_armv7h=(ghcup-$pkgver-$pkgrel-armv7h::https://downloads.haskell.org/~ghcup/$pkgver/armv7-linux-ghcup-$pkgver)
source_i686=(ghcup-$pkgver-$pkgrel-i686::https://downloads.haskell.org/~ghcup/$pkgver/i386-linux-ghcup-$pkgver)
sha256sums_x86_64=('70ca52b73ee796f5c43b4259f7fcedc2a0d60d85a6a9ed40a82ea8553fca34a0')
sha256sums_aarch64=('86df64134ab8ca6d4e8b0980e94fc36a447ff09ea823885034a3dd5617e840f3')
sha256sums_armv7h=('262cf5717700f40b7b43d7a65e50b17aec7292bd7e104dba1461e29f6252e7fc')
sha256sums_i686=('01bb5feeb15631d84163e67966b4d66461ef46a9ed36ff828b89adb558761241')
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
