# Maintainer: Hao Long <aur@esd.cc>

pkgname=httpx
pkgver=1.6.1
pkgrel=1
pkgdesc="A fast and multi-purpose HTTP toolkit allow to run multiple probers using retryablehttp library"
arch=("x86_64" "i686")
url="https://github.com/projectdiscovery/httpx"
license=("MIT")
provides=('httpx')
conflicts=('httpx' 'python-httpx')
depends=("glibc")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
b2sums=('044abc7ade2b6b279d07948eec0c4ea91c90ad9ef734d1a8a5bbb1cac48c58a03f94ee5383264c8b9a4d7d49e64115e6da93648208b0439dcf71ace820d99538')

build() {
  cd ${pkgname}-${pkgver}/cmd/${pkgname}
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm755 cmd/${pkgname}/${pkgname} ${pkgdir}/usr/bin/httpx-toolkit
  install -Dm644 LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
