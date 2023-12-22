# Maintainer: Filipe Nascimento <flipee at tuta dot io>
# Contributor: Sven Lechner <sven[dot]lechner[at]rwth-aachen[dot]de>

pkgname=act
pkgver=0.2.56
pkgrel=1
pkgdesc="Run your GitHub Actions locally"
arch=('i686' 'x86_64')
url="https://github.com/nektos/act"
license=('MIT')
depends=('docker')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('1af94bad393929299b51867b6455648a2ad82f30f657c1d5ee51c9996193c3e3')

build() {
    cd $pkgname-$pkgver

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"

    go build \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -ldflags "-linkmode=external -X main.version=$pkgver"
}

package() {
    cd $pkgname-$pkgver
    install -Dm755 $pkgname -t "$pkgdir/usr/bin"
    install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
    install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
