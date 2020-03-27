# Maintainer: Matthias Lisin <ml@visu.li>
pkgname=golangci-lint
pkgdesc="Linters Runner for Go. 5x faster than gometalinter."
pkgver=1.24.0
pkgrel=1
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url='https://github.com/golangci/golangci-lint'
license=('GPL3')
depends=('glibc')
makedepends=('git' 'go' 'gzip')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/golangci/golangci-lint/archive/v${pkgver}.tar.gz")
sha256sums=('d1f1441a966f090bf3f49e1737668a0b4c7eae5916d2bcaee48cca045e881f27')

build() {
  export CGO_LDFLAGS="$LDFLAGS"
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
  GOLANGCI_LINT_INSTALLED=true go test ./...
}

package() {
  cd "${pkgname}-${pkgver}"
  install -dm755 "$pkgdir"/usr/share/{bash-completion/completions,zsh/site-functions}
  install -Dm755 "$pkgname" "$pkgdir"/usr/bin/"$pkgname"
  ./"$pkgname" completion bash >"$pkgdir"/usr/share/bash-completion/completions/golangci-lint
  ./"$pkgname" completion zsh >"$pkgdir"/usr/share/zsh/site-functions/_golangci-lint
}
