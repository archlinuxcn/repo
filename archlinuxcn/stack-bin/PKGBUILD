# Maintainer: Phil Ruffwind <rf@rufflewind.com>
pkgname=stack-bin
pkgver=2.1.1
pkgrel=2
pkgdesc="The Haskell Tool Stack (tool only -- libraries not included)"
arch=(i686 x86_64)
url=https://hackage.haskell.org/package/stack
license=(BSD3)
depends=(gmp zlib)
provides=(stack)
conflicts=(stack)
source_aarch64=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-aarch64.tar.gz)
source_i686=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-i386.tar.gz)
source_x86_64=(https://github.com/commercialhaskell/stack/releases/download/v$pkgver/stack-$pkgver-linux-x86_64.tar.gz)
sha256sums_aarch64=('abedcb28d7e5a8e7ab2416d1de4b7988b4743acd926086a0ca6ad68859b2e5a1')
sha256sums_i686=('c541dd685fbe1c5bcb78db7e334f63d2f08e02e1c0d3c6c670f803a9f4ddcedb')
sha256sums_x86_64=('f53bb7a1e3f9bb097403c2df865a1e4e82a4a9bf15d7de1dacf4d620892816ef')

package() {
    cd "$srcdir/stack-$pkgver-linux-"*/
    install -Dm755 stack "$pkgdir/usr/bin/stack"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/stack/LICENSE"
}
