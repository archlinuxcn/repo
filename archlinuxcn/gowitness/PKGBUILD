# Maintainer: Hao Long <aur@esd.cc>

pkgname=gowitness
pkgver=3.2.0
pkgrel=1
pkgdesc="a golang, web screenshot utility using Chrome Headless"
arch=("x86_64" "i686")
url="https://github.com/sensepost/gowitness"
license=("GPL-3.0-or-later")
depends=("chromium")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
b2sums=('ce4485b059f72b7c28dfd0ca6970fd23d811489bd96c06baa05936fc15ba228c5e661d9c521d9f89d5472d0967bcd0f2da5b41edde7aa2a4f8f1e61dc70cc097')

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
