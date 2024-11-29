# Maintainer: Pig Fang <g-plane@hotmail.com>
# Maintainer: Mateusz Galazyn <carbolymer@gmail.com>
pkgname=cabal-install-bin
pkgver=3.12.1.0
pkgrel=1
pkgdesc="The command-line interface for Cabal and Hackage."
arch=(x86_64 aarch64)
url=https://www.haskell.org/cabal
license=(BSD)
depends=('glibc>=2.12')
provides=(cabal-install)
conflicts=(cabal-install)
source=(
  https://downloads.haskell.org/~cabal/cabal-install-$pkgver/cabal-install-$pkgver-$arch-linux-deb10.tar.xz
  https://downloads.haskell.org/~cabal/cabal-install-$pkgver/cabal-install-$pkgver.tar.gz
)
sha256sums=('8c94fbd54bb0d50ee2a079e8332f74d94f78fabd45270ef9aec9d7878f0e65ee'
            '6848acfd9c726fdcce544a8b669748d0fd9f2da26d28e841069dc4840276b1b2')

package() {
  install -Dm755 "$srcdir/cabal" "$pkgdir/usr/bin/cabal"
  install -Dm644 "$srcdir/cabal-install-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/cabal-install/LICENSE"
}
