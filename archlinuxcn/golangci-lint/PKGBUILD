# Maintainer: Matthias Lisin <ml@visu.li>
pkgname=golangci-lint
pkgdesc="Linters Runner for Go. 5x faster than gometalinter."
pkgver=1.23.6
_commit=b9eef79 # short commit hash of release
pkgrel=1
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url='https://github.com/golangci/golangci-lint'
license=('GPL3')
makedepends=('git' 'go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/golangci/golangci-lint/archive/v${pkgver}.tar.gz")
sha512sums=('95f7bb3477875a1a90ca8bd3be6dcc374d8c6e51c659165036e4ea13936c771491d25ddd93bb3ce10c49a6b3542aa4a167c8dda36933c78a148313d5cd3a5899')

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
    install -dm755 "$pkgdir"/usr/share/{bash-completion/completions,zsh/site-functions}
    install -Dm755 "$pkgname" "$pkgdir"/usr/bin/"$pkgname"
    "$pkgdir"/usr/bin/"$pkgname" completion bash > "$pkgdir"/usr/share/bash-completion/completions/golangci-lint
    "$pkgdir"/usr/bin/"$pkgname" completion zsh > "$pkgdir"/usr/share/zsh/site-functions/_golangci-lint
}
