# Maintainer: Pig Fang <g-plane@hotmail.com>
# Maintainer: Mateusz Galazyn <carbolymer@gmail.com>
pkgname=cabal-install-static
pkgver=3.18.2.0
pkgrel=1
pkgdesc="The command-line interface for Cabal and Hackage - static build."
arch=(x86_64 aarch64)
url=https://www.haskell.org/cabal
license=(BSD)
provides=(cabal-install)
conflicts=(cabal-install)
source=(https://downloads.haskell.org/~cabal/cabal-install-$pkgver/cabal-install-$pkgver.tar.gz)
source_x86_64=(https://downloads.haskell.org/~cabal/cabal-install-$pkgver/cabal-install-$pkgver-x86_64-linux-unknown.tar.xz)
source_aarch64=(https://downloads.haskell.org/~cabal/cabal-install-$pkgver/cabal-install-$pkgver-aarch64-linux-unknown.tar.xz)
sha256sums=('1d55fea99bf82b2f4a2ae51bd47313167048ba05aac6290a30752d91cd5f7cb8')
sha256sums_x86_64=('b4f4c83135da77cfc18ccd6056398ca714a2dad86d5f635621ffdda8f9afe587')
sha256sums_aarch64=('e4d940131ab0b78943a4b5ce64a9ef5acc452ea849df197787eaeecb1c3bf276')

package() {
  install -Dm755 "$srcdir/cabal" "$pkgdir/usr/bin/cabal"
  install -Dm644 "$srcdir/cabal-install-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/cabal-install/LICENSE"
}
