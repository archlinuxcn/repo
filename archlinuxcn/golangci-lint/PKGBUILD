# Maintainer: Matthias Lisin <ml@visu.li>
pkgname=golangci-lint
pkgdesc="Linters Runner for Go. 5x faster than gometalinter."
pkgver=1.21.0
_commit=645e794 # short commit hash of release
pkgrel=1
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url='https://github.com/golangci/golangci-lint'
license=('GPL3')
makedepends=('git' 'go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/golangci/golangci-lint/archive/v${pkgver}.tar.gz")
sha512sums=('cdb1aa23fbb0422e3ffc9b880a21e87e88e1251423c516c270c4c598831736554ed977396cd3ebd3ce891ac2eea9509af4a682c4ebd62c230fcb88dc6131b78a')

build() {
    cd "${pkgname}-${pkgver}"
    export GOPATH="$srcdir"
    # ISO-8601, like the official binary
    _date=$(date -u -Iseconds -d "@${SOURCE_DATE_EPOCH}" | sed 's/+00:00/Z/')
    go build -trimpath \
             -ldflags "-X 'main.version=${pkgver}' \
                       -X 'main.commit=${_commit}' \
                       -X 'main.date=${_date}' \
                       -extldflags=${LDFLAGS}" \
             -buildmode=pie -o "$pkgname" ./cmd/"$pkgname"
}

package() {
    cd "${pkgname}-${pkgver}"
    install -Dm755 "$pkgname" "$pkgdir"/usr/bin/"$pkgname"
}
