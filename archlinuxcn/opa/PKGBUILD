# Maintainer: Jonathan Wright <jon@than.io>
# Prior Maintainer: Brian Atkinson <brian@atkinson.mn>
# Prior Maintainer: David Birks <david@birks.dev>

pkgname=opa
pkgver=1.5.1
pkgrel=1
pkgdesc='Command-line utility and REPL for Open Policy Agent'
arch=(x86_64)
url='https://github.com/open-policy-agent/opa'
license=(Apache)
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/open-policy-agent/opa/archive/v$pkgver.tar.gz")
sha256sums=('ea34c1f9a27501d0c6313f96bf33665333c395536bf6a849c6d0253c5a807795')

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -modcacherw"

  go build \
  -ldflags "-X github.com/open-policy-agent/opa/version.Version=$pkgver" \
  -o "$pkgname" \
  .

  mkdir completion
  "./$pkgname" completion bash > "completion/$pkgname"
  "./$pkgname" completion zsh > "completion/_$pkgname"
  "./$pkgname" completion fish > "completion/$pkgname.fish"
}

package() {
  install -Dm 755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -vDm 644 "$srcdir/$pkgname-$pkgver/completion/$pkgname" -t "$pkgdir/usr/share/bash-completion/completions/"
  install -vDm 644 "$srcdir/$pkgname-$pkgver/completion/_$pkgname" -t "$pkgdir/usr/share/zsh/site-functions/"
  install -vDm 644 "$srcdir/$pkgname-$pkgver/completion/$pkgname.fish" -t "$pkgdir/usr/share/fish/completions/"
}
