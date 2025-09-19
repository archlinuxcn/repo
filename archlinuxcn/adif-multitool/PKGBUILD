# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=adif-multitool
pkgver=0.1.21
pkgrel=1
pkgdesc='Validate, modify, and convert ham radio log files with a handy command-line tool'
url='https://github.com/flwyd/adif-multitool'
arch=('x86_64')
license=('Apache-2.0')
depends=('glibc')
makedepends=('go')
source=("${url}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('ef82b287eda555fb3fb4b6874ca2a01db41208882c76e590caaa12b6641d9b79')
b2sums=('e6ca103cc340be4ca3dd40639916bf35244cdd80567b8416e339b60e07957fdec23dd2e2cf0580502e80ccd6f1b7e636c07b7c8071c1cb474ddb80576dc12c6e')

prepare(){
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build -o build ./adifmt
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/adifmt "$pkgdir"/usr/bin/$pkgname
}

# vim: ts=2 sw=2 et:
