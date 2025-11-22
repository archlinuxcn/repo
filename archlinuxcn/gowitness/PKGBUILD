# Maintainer: Hao Long <aur@esd.cc>

pkgname=gowitness
pkgver=3.1.0
pkgrel=1
pkgdesc="a golang, web screenshot utility using Chrome Headless"
arch=("x86_64" "i686")
url="https://github.com/sensepost/gowitness"
license=("GPL-3.0-or-later")
depends=("chromium")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('4fdd1fca6e2632f9a9d9124a837e406f01fbf09b8cdebd963705fea7168776ec8473acdc6fbc938a0a33007c8432992bdaf2d981c83974e5127923cbbbee6b77')

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
