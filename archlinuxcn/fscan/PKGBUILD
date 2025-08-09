# Maintainer: Misaka13514 <Misaka13514 at gmail dot com>
pkgname=fscan
pkgver=2.0.2
_pkgver=${pkgver//_/-}
pkgrel=1
pkgdesc="An intranet comprehensive scanning tool"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/shadow1ng/fscan"
license=('MIT')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz"::"$url/archive/v$_pkgver.tar.gz")
sha256sums=('bd82a5381ea1b5e97a429fb6c1331742d697b3753c56afd620598ff840394122')

prepare() {
    cd "$pkgname-$_pkgver"
    mkdir -p build/
}

build() {
    cd "$pkgname-$_pkgver"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
    go build -o build .
}

check() {
    cd "$pkgname-$_pkgver"
    go test ./...
}

package() {
    cd "$pkgname-$_pkgver"
    install -Dm755 -t "$pkgdir/usr/bin/" build/$pkgname
    install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.txt
    install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" *.md
}
