# Maintainer: axionl <axionl@aosc.io>
pkgname=baidupcs-go-git
pkgver=r325.82a3979
pkgrel=1
pkgdesc="The terminal utility for Baidu Network Disk (Golang Version)."
arch=('x86_64')
makedepends=('git' 'go')
depends=('glibc')
conflicts=("baidupcs")
provides=("baidupcs")
url="https://github.com/iikira/BaiduPCS-Go"
license=("Apache")

source=("$pkgname::git+https://github.com/iikira/BaiduPCS-Go"
    "https://raw.githubusercontent.com/iikira/BaiduPCS-Go/master/LICENSE")

sha256sums=('SKIP'
    'ddadea2805326e3cb072a8b6769885fc1399475922e4c7d60f5e9f8e28c63e3d')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    export GOPATH="$srcdir/build"
    cd "$srcdir/$pkgname/"
    go get -u -v github.com/iikira/BaiduPCS-Go
}

package() {
    dir="$srcdir/build/bin"
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/baidupcs-go-git/LICENSE
    cd $dir
    install -Dm755 BaiduPCS-Go ${pkgdir}/usr/bin/baidupcs
    echo "README FILE: https://github.com/iikira/BaiduPCS-Go/blob/master/README.md"
}
