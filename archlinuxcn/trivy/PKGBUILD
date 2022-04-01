# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=trivy
pkgver=0.25.0
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
b2sums=('38cda5c6def31ea7c27207cd618daf069c79321830ed5bd0e53778f5b4fb55d1f777a3788e8d6cc201f540cb99b60f6ce6b4304f22478e83a08ea2f5674d5cb6')

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
