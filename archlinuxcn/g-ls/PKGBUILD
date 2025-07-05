# Maintainer: Equationzhao <equationzhao at foxmail dot com>
pkgname='g-ls'
pkgver=0.31.0
pkgrel=1
pkgdesc='a powerful ls in golang'
arch=('x86_64' 'aarch64')
url='https://github.com/Equationzhao/g'
license=('MIT')
makedepends=('go')
backup=("etc/$pkgname/config.conf")
source=("g-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('122ca7ebf32ab2aada05cd513d44b55082d9bcfa9b890ee0ff60fdebfea06d0c')

build() {
    cd "$srcdir/g-$pkgver"
    go build -ldflags="-s -w" -o g
}

package() {
    cd "$srcdir/g-$pkgver"
    mkdir -p "$pkgdir/usr/bin"
    install -m755 g "$pkgdir/usr/bin"
    cd man
    install -Dm644 g.1.gz "$pkgdir/usr/share/man/man1/g.1.gz"
}
