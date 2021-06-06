# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.14.1
pkgrel=2
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
sha256sums_x86_64=('59e31b2ede3ed20f79dce0f8ba0a68b6fb25e5f00ba2d7243f6a8af68d979ff5')
sha256sums_aarch64=('e9ae07b7d41ea03e6af9c1f3587f61287827c4e29478b6a5d46ea1ce5af4cee5')
sha256sums_armv7h=('646832030efbc0a848df24c08b5eb7507bd15d1c2eb95fea6d9d03890f3662be')
sha256sums_i686=('610aac7c3be3ba3874c07b9cae5b2ca0da9a92bf381afc2597bd2dc9c70aae0c')
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
