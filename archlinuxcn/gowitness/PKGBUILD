# Maintainer: Hao Long <aur@esd.cc>

pkgname=gowitness
pkgver=2.3.2
pkgrel=1
pkgdesc="a golang, web screenshot utility using Chrome Headless"
arch=("x86_64" "i686")
url="https://github.com/sensepost/gowitness"
license=("GPL3")
depends=("chromium")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('c3541d36ff3cb88f7e5022a7dd67b0dd33461b99c7f344a0fa90de95696137ed')

build() {
  cd ${pkgname}-${pkgver}
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm755 gowitness ${pkgdir}/usr/bin/${pkgname}
}
