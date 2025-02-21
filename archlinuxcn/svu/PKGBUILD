# Maintainer: tarball <bootctl@gmail.com>
# Contributor: ml <>

pkgname=svu
pkgver=3.1.0
pkgrel=1
pkgdesc='Semantic Version Util'
arch=(i686 x86_64 armv7h armv6h aarch64 riscv64)
url='https://github.com/caarlos0/svu'
license=('MIT')
depends=('git')
makedepends=('go')
source=("$url/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('21ba12f979623f8e72cf0139337d49733ef084298b39a81287d02680f54d50a9')
_go_flags=(-ldflags "-linkmode=external -X main.version=v$pkgver")

build() {
  cd "$pkgname-$pkgver"
  export CGO_ENABLED=1
  export CGO_LDFLAGS="$LDFLAGS"
  export CGO_CFLAGS="$CFLAGS"
  export CGO_CPPFLAGS="$CPPFLAGS"
  export CGO_CXXFLAGS="$CXXFLAGS"
  export GOFLAGS='-buildmode=pie -trimpath -modcacherw'
  go build -o "$pkgname" "${_go_flags[@]}" main.go
}

check() {
  cd "$pkgname-$pkgver"
  go test -v -short "${_go_flags[@]}" .
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "$pkgname" -t "$pkgdir/usr/bin"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE.md -t "$pkgdir/usr/share/licenses/$pkgname"
}
