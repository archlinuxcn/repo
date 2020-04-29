# Maintainer: Matthias Lisin <ml@visu.li>
pkgname=golangci-lint
pkgdesc="Linters Runner for Go. 5x faster than gometalinter."
pkgver=1.25.1
pkgrel=6
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url='https://github.com/golangci/golangci-lint'
license=('GPL3')
depends=('glibc')
makedepends=('git' 'go' 'gzip')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/golangci/golangci-lint/archive/v${pkgver}.tar.gz")
sha256sums=('034440e00f81d1b5adfe5e39bceb2f0b9cb19066195a61e750a4982bbe512cf3')

prepare() {
  cd "${pkgname}-${pkgver}"
  go mod download
}

build() {
  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export GOFLAGS='-buildmode=pie -trimpath -modcacherw'
  _commit=$(zcat "${pkgname}-${pkgver}.tar.gz" | git get-tar-commit-id)
  _flags=(
    -X=main.version=$pkgver
    -X=main.commit=${_commit::7}
    -X=main.date=$(date -u -d "@${SOURCE_DATE_EPOCH}" +'%FT%TZ')
  )
  cd "${pkgname}-${pkgver}"
  go build -o "$pkgname" -ldflags="${_flags[*]}" ./cmd/"$pkgname"
}

check() {
  cd "${pkgname}-${pkgver}"
  # some tests build the binary and overwrite our build
  chmod 555 "$pkgname" # canary
  unset CGO_LDFLAGS CGO_CFLAGS GOFLAGS
  GOLANGCI_LINT_INSTALLED=true go test ./...
}

package() {
  cd "${pkgname}-${pkgver}"
  install -dm755 "$pkgdir"/usr/share/{bash-completion/completions,zsh/site-functions}
  install -Dm755 "$pkgname" "$pkgdir"/usr/bin/"$pkgname"
  ./"$pkgname" completion bash >"$pkgdir"/usr/share/bash-completion/completions/golangci-lint
  ./"$pkgname" completion zsh >"$pkgdir"/usr/share/zsh/site-functions/_golangci-lint
}
