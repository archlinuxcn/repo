# Maintainer: OpenSorcerer <alex cat fossfed dog eu>
pkgname=xcaddy
pkgver=0.4.4
pkgrel=1
pkgdesc="Build Caddy with plugins"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://github.com/caddyserver/xcaddy"
license=('Apache-2.0')
depends=('go')
makedepends=('git')
source=("git+$url.git#tag=v$pkgver")
sha512sums=('SKIP')

build() {
    cd "$pkgname"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
    go build -o xcaddy "cmd/$pkgname/main.go"
}

package() {
    cd "$pkgname"
    install -Dm755 "./xcaddy" "$pkgdir/usr/bin/xcaddy"
}
