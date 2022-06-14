# Maintainer: tdewolff <tacodewolff@gmail.com>
# Maintainer: 4679kun <4679kun@outlook.com>
# Maintainer: meepzh <meep.aur@meepzh.com>

pkgname=minify
pkgver=2.11.10
pkgrel=1
pkgdesc="Minifier CLI for HTML, CSS, JS, JSON, SVG and XML"
arch=('x86_64')
url="https://github.com/tdewolff/minify"
license=('MIT')
makedepends=('go')
optdepends=('bash-completion: command-line autocomplete with bash')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('ace21c2009e094c3e985865f52b51e6f20d2b257c3a1335a9d7f3e48b38f6530')

prepare() {
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"
  export CGO_ENABLED=0
  go build -trimpath -buildmode=pie -mod=readonly -modcacherw \
           -ldflags "-X 'main.Version=v$pkgver'" -o build ./cmd/minify
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "build/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "cmd/minify/bash_completion" "$pkgdir/usr/share/bash-completion/completions/$pkgname"
  source cmd/minify/bash_completion
}

