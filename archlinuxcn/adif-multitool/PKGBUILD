# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=adif-multitool
pkgver=0.1.22
pkgrel=1
pkgdesc='Validate, modify, and convert ham radio log files with a handy command-line tool'
url='https://github.com/flwyd/adif-multitool'
arch=('x86_64')
license=('Apache-2.0')
depends=('glibc')
makedepends=('go')
source=("${url}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('5a13ffb5407fb22d4ee977ce8b12551a2b1bef4f463fc497ed3c13a064af7b7e')
b2sums=('29d091e51981ee27fa20c1cea40d791304795dba8b399e7d2751f59594e167c9b797ea87334f19bd0e43df1d73097930f6cb18b972dc7e60c9679f1c459fa7e5')

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
