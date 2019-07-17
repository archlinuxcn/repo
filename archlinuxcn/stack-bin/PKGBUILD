# Maintainer: Phil Ruffwind <rf@rufflewind.com>
pkgname=stack-bin
pkgver=2.1.3
pkgrel=1
pkgdesc="The Haskell Tool Stack (tool only -- libraries not included)"
arch=(aarch64 i686 x86_64)
url=https://hackage.haskell.org/package/stack
license=(BSD3)
depends=(gmp zlib)
provides=(stack)
conflicts=(stack)
source_aarch64=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-aarch64.tar.gz)
source_i686=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-i386.tar.gz)
source_x86_64=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-x86_64.tar.gz)
sha256sums_aarch64=('1212c3ef9c4e901c50b086f1d778c28d75eb27cb4529695d2f1a16ea3f898a6d')
sha256sums_i686=('4acd97f4c91b1d1333c8d84ea38f690f0b5ac5224ba591f8cdd1b9d0e8973807')
sha256sums_x86_64=('c724b207831fe5f06b087bac7e01d33e61a1c9cad6be0468f9c117d383ec5673')

package() {
    cd "$srcdir/stack-$pkgver-linux-"*/
    install -Dm755 stack "$pkgdir/usr/bin/stack"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/stack/LICENSE"
}
