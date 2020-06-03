# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=trivy
pkgver=0.9.0
pkgrel=1
pkgdesc="A Simple and Comprehensive Vulnerability Scanner for Containers, Suitable for CI"
arch=("x86_64" "i686")
url="https://github.com/aquasecurity/trivy"
license=("Apache")
depends=("device-mapper")
optdepends=("rpm: RHEL/CentOS based image support")
makedepends=("go-pie" "btrfs-progs")
provides=('trivy')
conflicts=('trivy')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('1f72d3cd0264c9d363a3b0aff727f953f73358e0cbb94335be446ee7085e7bd3')

build() {
  cd ${pkgname}-${pkgver}/cmd/trivy
  go build -trimpath -ldflags "-extldflags ${LDFLAGS}" .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm755 cmd/trivy/${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
