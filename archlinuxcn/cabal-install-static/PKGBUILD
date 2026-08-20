# Maintainer: Pig Fang <g-plane@hotmail.com>
# Maintainer: Mateusz Galazyn <carbolymer@gmail.com>
pkgname=cabal-install-static
pkgver=3.18.1.0
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
sha256sums=('7e5c3f5e53f7c91f9ff8f0fb075574e772562d0eeb400c402c7d9277558f0821')
sha256sums_x86_64=('c6385c155ff61f792dfed0e8c101004db63f8d8b556dd6c9838f81a012bf28a6')
sha256sums_aarch64=('b8333291622c0354d72adec64ccb19e13563264bae2c15c9e6657e7f9c1486e8')

package() {
  install -Dm755 "$srcdir/cabal" "$pkgdir/usr/bin/cabal"
  install -Dm644 "$srcdir/cabal-install-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/cabal-install/LICENSE"
}
