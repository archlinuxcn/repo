# Maintainer: tdewolff <tacodewolff@gmail.com>
# Maintainer: 4679kun <4679kun@outlook.com>
# Maintainer: meepzh <meep.aur@meepzh.com>

pkgname=minify
pkgver=2.22.2
pkgrel=1
pkgdesc="Minifier CLI for HTML, CSS, JS, JSON, SVG and XML"
arch=('any')
url="https://github.com/tdewolff/minify"
license=('MIT')
makedepends=('go')
optdepends=('bash-completion: command-line autocomplete with bash')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('456738e7f477ace8f6f94cbc313f7eb8047c2fc11573a35fb37bfc495032d9ca')

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

