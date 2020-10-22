# Maintainer: Christian Muehlhaeuser <muesli at gmail dot com>

pkgname=duf
pkgver=0.4.0
pkgrel=1
pkgdesc="Disk Usage/Free Utility"
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/muesli/duf"
license=('MIT')
makedepends=('go')
source=("${url}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('da6b0bb601d7b9a92cfd41005eae7a66573d28e77625f4e747b285207980784b')

prepare() {
    export GOPATH="$srcdir/gopath"
    go clean -modcache
}

build() {
    cd "$pkgname-$pkgver"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"

    go build \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -ldflags "-X main.Version=$pkgver -linkmode external -extldflags \"${LDFLAGS}\"" \
        -o "$pkgname" .

    go clean -modcache
}

package() {
    cd "$pkgname-$pkgver"

    install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=4 sw=4 et:
