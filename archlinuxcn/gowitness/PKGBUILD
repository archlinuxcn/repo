# Maintainer: Hao Long <aur@esd.cc>

pkgname=gowitness
pkgver=2.3.3
pkgrel=1
pkgdesc="a golang, web screenshot utility using Chrome Headless"
arch=("x86_64" "i686")
url="https://github.com/sensepost/gowitness"
license=("GPL3")
depends=("chromium")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('ec57b7efc28bdb7f2ac3b521f8871594b78c389455f4fc0d8826c3276814bd76')

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
