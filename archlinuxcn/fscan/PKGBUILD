# Maintainer: Misaka13514 <Misaka13514 at gmail dot com>
pkgname=fscan
pkgver=2.0.0_build4
_pkgver=${pkgver//_/-}
pkgrel=1
pkgdesc="An intranet comprehensive scanning tool"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/shadow1ng/fscan"
license=('MIT')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz"::"$url/archive/$_pkgver.tar.gz")
sha256sums=('a45c945415d5c5598c1d44cb1c92c8e2022eb727f745c816d46d1c71c2edc5a0')

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
