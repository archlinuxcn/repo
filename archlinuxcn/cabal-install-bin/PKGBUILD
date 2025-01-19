# Maintainer: Pig Fang <g-plane@hotmail.com>
# Maintainer: Mateusz Galazyn <carbolymer@gmail.com>
pkgname=cabal-install-bin
pkgver=3.14.1.1
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
sha256sums=('aa03c01484129d8fbb0462550f94afa435cd241e5cfa7e75ee9bf1a510d96916'
            '0bd0e1d36025e96bc54480295762944a319315e021c59258cac07d34e5bb4533')

package() {
  install -Dm755 "$srcdir/cabal" "$pkgdir/usr/bin/cabal"
  install -Dm644 "$srcdir/cabal-install-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/cabal-install/LICENSE"
}
