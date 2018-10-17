# Maintainer: Phil Ruffwind <rf@rufflewind.com>
pkgname=stack-bin
pkgver=1.9.1
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
sha256sums_i686=('5f16e28209a303252c2a8651f3e886ad0338d31bc859886b07813cbdffd78987')
sha256sums_x86_64=('6987c8910ac7f5b6a64e40d3a3fe2264406d9086df4fb93e5e749f7cb69b53d6')

package() {
    cd "$srcdir/stack-$pkgver-linux-"*/
    install -Dm755 stack "$pkgdir/usr/bin/stack"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/stack/LICENSE"
}
