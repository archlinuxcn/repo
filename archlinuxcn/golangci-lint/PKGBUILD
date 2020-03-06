# Maintainer: Matthias Lisin <ml@visu.li>
pkgname=golangci-lint
pkgdesc="Linters Runner for Go. 5x faster than gometalinter."
pkgver=1.23.8
_commit=76a82c6 # short commit hash of release
pkgrel=1
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url='https://github.com/golangci/golangci-lint'
license=('GPL3')
makedepends=('git' 'go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/golangci/golangci-lint/archive/v${pkgver}.tar.gz")
sha512sums=('fc393b2b6f5142cd260db9f3a1b7b11487d11d828ae69ad5e3130e2b2283e715f8d3d1fb2309da91eee7b03bd534c3a7479d5fe437dd338b3d211bfa93e92b3d')

build() {
    cd "${pkgname}-${pkgver}"
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
