# Maintainer: amesgen <amesgen AT amesgen DOT de>
pkgname=ghcup-hs-bin
pkgver=0.1.17.2
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
sha256sums_x86_64=('e9adb022b9bcfe501caca39e76ae7241af0f30fbb466a2202837a7a578607daf')
sha256sums_aarch64=('ad72641877f91f1cc5142151dafad68566f439114f96a738837ed549430173a5')
sha256sums_armv7h=('03f2f8aaa8393372e9f7e16061703eda3f497b9604171825995389f3d5cc8f8f')
sha256sums_i686=('eb29a33ed9798c94ed05b10c66c2cd6690a4d5aa79ed7ce6a9b8564e0c095ff4')
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
