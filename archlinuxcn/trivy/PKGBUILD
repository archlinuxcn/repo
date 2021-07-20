# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=trivy
pkgver=0.19.1
pkgrel=1
pkgdesc="A Simple and Comprehensive Vulnerability Scanner for Containers, Suitable for CI"
arch=("x86_64" "i686")
url="https://github.com/aquasecurity/trivy"
license=("Apache")
depends=("device-mapper")
optdepends=("rpm: RHEL/CentOS based image support")
makedepends=("go" "btrfs-progs")
provides=('trivy')
conflicts=('trivy')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('3966e0159d891e107e3080420606a0ee7b828a96e4a36e2b275fdb39cc6b2516')

build() {
  cd ${pkgname}-${pkgver}/cmd/trivy
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
  install -Dm755 cmd/trivy/${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
