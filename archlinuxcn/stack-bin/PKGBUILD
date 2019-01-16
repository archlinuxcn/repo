# Maintainer: Phil Ruffwind <rf@rufflewind.com>
pkgname=stack-bin
pkgver=1.9.3
pkgrel=1
pkgdesc="The Haskell Tool Stack (tool only -- libraries not included)"
arch=(i686 x86_64)
url=https://hackage.haskell.org/package/stack
license=(BSD3)
depends=(gmp zlib)
provides=(stack)
conflicts=(stack)
source_i686=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-i386.tar.gz)
source_x86_64=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-x86_64.tar.gz)
sha256sums_i686=('c7a45fcf782fcc9b2bbac38f9e1b41afec5e940c6e26936a51652f246e226505')
sha256sums_x86_64=('e2363728e5818ccc68db9371c15af892a9a1fc86d808d0a9a77257f13696e946')

package() {
    cd "$srcdir/stack-$pkgver-linux-"*/
    install -Dm755 stack "$pkgdir/usr/bin/stack"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/stack/LICENSE"
}
