# Maintainer: tdewolff <tacodewolff@gmail.com>
# Maintainer: 4679kun <4679kun@outlook.com>
# Maintainer: meepzh <meep.aur@meepzh.com>

pkgname=minify
pkgver=2.24.13
pkgrel=1
pkgdesc="Minifier CLI for HTML, CSS, JS, JSON, SVG and XML"
arch=('any')
url="https://github.com/tdewolff/minify"
license=('MIT')
makedepends=('go')
optdepends=('bash-completion: command-line autocomplete with bash')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('d81dc3e0793d9a69e24d3655f60cf19be8c5cb62f86f6c3a3a4e7b678bc9b31c')

prepare() {
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"
  go build -trimpath -buildmode=pie -mod=readonly -modcacherw \
           -ldflags "-linkmode external -extldflags \"${LDFLAGS}\" -X 'main.Version=v$pkgver'" -o build/minify ./cmd/minify
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
  source cmd/minify/bash_completion
}

