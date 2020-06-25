# Maintainer: DuckSoft <realducksoft at gmail dot com>
pkgname=pingtunnel-git
_pkgname=${pkgname%-git}
pkgver=2.3.r0.ga575bab
pkgrel=1
pkgdesc="A tool that advertises TCP/UDP/SOCKS5 traffic as ICMP traffic for forwarding."
depends=(glibc)
optdepends=('geoip-database: geolite country database')
provides=($_pkgname)
conflicts=($_pkgname)
makedepends=(go git)
arch=(x86_64)
license=(MIT)
url="https://github.com/esrrhs/pingtunnel"
source=("$_pkgname::git+$url.git")
sha512sums=('SKIP')

pkgver() {
    cd "$srcdir"/$_pkgname
    git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    # NOTE: uncomment this if you are in mainland china
    # export GOPROXY="https://goproxy.cn,direct"
    export CGO_ENABLED=1
    export GO111MODULE=off
    
    cd "$srcdir"/$_pkgname
    go get -v -t -d ./...
    go build -v \
        -buildmode=pie -trimpath \
        -ldflags="-s -w -extldflags=-Wl,-z,now,-z,relro" \
        -o pingtunnel .
}

package() {
    install -Dm755 -t "$pkgdir"/usr/bin/ "$srcdir"/$_pkgname/pingtunnel
    install -Dm644 -t "$pkgdir"/usr/share/doc/pingtunnel/ "$srcdir"/$_pkgname/*.{md,jpg}
}
