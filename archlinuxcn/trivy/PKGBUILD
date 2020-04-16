# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=trivy
pkgver=0.6.0
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
sha256sums=('b0f57d512ee77b41972acc11ac362a4532489dc5c957bc57d328ab1c18449169')

build() {
  cd ${pkgname}-${pkgver}/cmd/trivy
  go build -trimpath -ldflags "-extldflags ${LDFLAGS}" .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm755 cmd/trivy/${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
