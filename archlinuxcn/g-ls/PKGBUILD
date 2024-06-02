# Maintainer: Equationzhao <equationzhao at foxmail dot com>
pkgname='g-ls'
pkgver=0.28.2
pkgrel=3
pkgdesc='a powerful ls in golang'
arch=('x86_64' 'aarch64')
url='https://github.com/Equationzhao/g'
license=('MIT')
makedepends=('go')
backup=("etc/$pkgname/config.conf")
source=("g-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('05df40665ea8c402c9d76b29269edb721758e9913bc03d173e7e84fa7a0a2ab6')

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
