# Maintainer: cubercsl <2014cais01 at gmail dot com>
# Contributor:  mzz2017 < mzz at tuta dot io>

pkgname=gg
pkgver=0.2.13
pkgrel=2
provides=('gg')
pkgdesc='A command-line tool for one-click proxy in your research and development without installing v2ray or anything else (only for linux).'
arch=('x86_64' 'aarch64' 'arm' 'armv7h' 'armv6h' 'armv7l')
url='https://github.com/mzz2017/gg'
license=('AGPL')
depends=('glibc')
makedepends=('go')
optdepends=('libcap: for setcap')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
        gg-cap
        gg.hook)
sha256sums=('73d624f6cfcc003a1d1cac61b9a314dd29da745570c73660a4a5f9e201ec7b7f'
            'd06e64e7de16390d09f7c980446262733eddf0bc589b5c32dde651be1c24e741'
            '7cec4ef2c0681366ec729e673db0411e69da5b08b8d23da7628bd6bac3a233cc')
install=$pkgname.install

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
    # setcap for gg
    install -Dm644 $srcdir/gg.hook "$pkgdir"/usr/share/libalpm/hooks/gg.hook
    install -Dm755 $srcdir/gg-cap "$pkgdir"/usr/share/libalpm/scripts/gg-cap
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    go test ./...
}
