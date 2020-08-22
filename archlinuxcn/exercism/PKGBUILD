# Maintainer: Federico Squartini <federico.squartini at gmail dot com>

pkgname=exercism
pkgver=3.0.13
pkgrel=1
pkgdesc="Command line client for https://exercism.io"
arch=("i686" "x86_64")
url="https://github.com/exercism/cli"
license=("MIT")
depends=('glibc')
makedepends=('go-pie')
source=("https://github.com/exercism/cli/archive/v${pkgver}.tar.gz")
sha256sums=('ecc27f272792bc8909d14f11dd08f0d2e9bde4cc663b3769e00eab6e65328a9f')

prepare() {
  export GOPATH="$srcdir"/.gopath
  mkdir -p "$GOPATH"/src/github.com/exercism
  ln -sf "$srcdir"/cli-$pkgver "$GOPATH"/src/github.com/exercism/cli
}

build() {
  export GOPATH="$srcdir"/.gopath
  cd "$GOPATH"/src/github.com/exercism/cli
  go build -o out/exercism exercism/main.go
}

package(){
  cd $srcdir/cli-${pkgver}
  install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -D -m644 shell/exercism_completion.bash "$pkgdir/usr/share/$pkgname/completion/exercism_completion.bash"
  install -D -m644 shell/exercism_completion.zsh "$pkgdir/usr/share/$pkgname/completion/exercism_completion.zsh"
  install -D out/exercism "$pkgdir/usr/bin/exercism"
}
