# Maintainer: Haochen Tong <i at hexchain dot org>

pkgname=elvish
pkgver=0.6
pkgrel=1
pkgdesc="A friendly and expressive Unix shell."
arch=('i686' 'x86_64')
url="https://github.com/elves/elvish"
license=('custom:2-clause BSD')
provides=('elvish')
makedepends=('git' 'go')
depends=('glibc')
source=("git+https://github.com/elves/elvish.git#tag=$pkgver")
md5sums=('SKIP')
install=elvish.install

prepare() {
    cd "$srcdir"

    mkdir -p build/src/github.com/elves
    ln -sf "$srcdir/$pkgname" build/src/github.com/elves/
    export GOPATH="$srcdir/build"
}

build() {
    cd "$GOPATH/src/github.com/elves/elvish"
    make get
}

check() {
    cd "$GOPATH/src/github.com/elves/elvish"
    make test
}

package() {
    install -Dm755 "$srcdir/build/bin/elvish" -t "$pkgdir/usr/bin/"
    install -Dm644 "$srcdir/$pkgname/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
