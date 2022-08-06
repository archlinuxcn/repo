# Maintainer: cubercsl <2014cais01 at gmail dot com>
# Contributor:  mzz2017 < mzz at tuta dot io>

pkgname=gg
pkgver=0.2.8
pkgrel=1
provides=('gg')
pkgdesc='A command-line tool for one-click proxy in your research and development without installing v2ray or anything else (only for linux).'
arch=('x86_64' 'aarch64' 'arm' 'armv7h' 'armv6h' 'armv7l')
url='https://github.com/mzz2017/gg'
license=('AGPL')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('d2312eb3feaa331e9139ab5f683516baa9cd8551753a6be59b902214c64b6021')

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
    install -Dm644 completion/bash/gg -t "$pkgdir/usr/share/bash-completion/completions"
    install -Dm644 completion/zsh/_gg -t "$pkgdir/usr/share/zsh/site-functions"
    install -Dm644 completion/fish/gg.fish -t "$pkgdir/usr/share/fish/vendor_completions.d"
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    go test ./...
}
