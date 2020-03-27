# Maintainer: axionl <axionl@aosc.io>
pkgname=baidupcs-go-git
pkgver=3.6.1.r4.g662feec
pkgrel=1
pkgdesc="The terminal utility for Baidu Network Disk (Golang Version)."
arch=('x86_64')
depends=('glibc')
makedepends=('git' 'go-pie')
conflicts=("baidupcs")
provides=("baidupcs")
url="https://github.com/iikira/BaiduPCS-Go"
license=("Apache")

source=("${pkgname}::git+https://github.com/iikira/BaiduPCS-Go")
sha256sums=('SKIP')

pkgver() {
    cd "${pkgname}"

    ( set -o pipefail
      git describe --long --tags 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' ||
      printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
    )
}

build() {
    cd "${pkgname}"
    CGO_ENABLED=0 go build -x -v -ldflags "-extldflags ${LDFLAGS} -X main.Version=${pkgver} -s -w"
}

package() {
    cd "${pkgname}"
    install -Dm755 BaiduPCS-Go "${pkgdir}/usr/bin/baidupcs"
    install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
