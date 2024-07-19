# Maintainer: Hao Long <aur@esd.cc>

pkgname=httpx
pkgver=1.6.6
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
b2sums=('5ea27beaee08d9de4964a93bd5677a23c65a9bee8e14c271b5ed6c92120c233911e213d139d1f0501397de7dc0d8d3f6f17ca885655764b3771b874b3a98356f')

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
