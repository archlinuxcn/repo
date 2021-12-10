# Maintainer: cubercsl <2014cais01 at gmail dot com>
# Contributor:  mzz2017 < mzz at tuta dot io>

pkgname=gg
pkgver=0.1.12
pkgrel=3
provides=('gg')
pkgdesc='A command-line tool for one-click proxy in your research and development without installing v2ray or anything else (only for linux). '
arch=('x86_64' 'aarch64' 'arm' 'armv7h' 'armv6h' 'armv7l')
url='https://github.com/mzz2017/gg'
license=('AGPL')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('66943ca4b7fe4d34a4c313d79200189ca69b9de58e421622005d1d3441ae52fa')

prepare(){
    cd "$srcdir/$pkgname-$pkgver"
    mkdir -p build/
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
    go build -ldflags="-X github.com/mzz2017/gg/cmd.Version=$pkgver -linkmode=external" -o build ./...
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm755 build/$pkgname "$pkgdir"/usr/bin/$pkgname
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    go test ./...
}
