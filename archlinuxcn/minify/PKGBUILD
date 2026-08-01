# Maintainer: tdewolff <tacodewolff@gmail.com>
# Maintainer: 4679kun <4679kun@outlook.com>
# Maintainer: meepzh <meep.aur@meepzh.com>

pkgname=minify
pkgver=2.24.14
pkgrel=2
pkgdesc="Minifier CLI for HTML, CSS, JS, JSON, SVG and XML"
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/tdewolff/minify"
license=('MIT')
depends=(glibc)
makedepends=('go')
optdepends=('bash-completion: command-line autocomplete with bash')
options=('!lto')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('bb5b9bdf52ccd19a1d5e69f867fabf7355ae124ba114e933b72a88a8cea20d90')

prepare() {
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

  go build -ldflags "-linkmode=external -extldflags \"${LDFLAGS}\" -X 'main.Version=v$pkgver'" -o build/minify ./cmd/minify
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/minify "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "cmd/minify/bash_completion" "$pkgdir/usr/share/bash-completion/completions/$pkgname"
}

