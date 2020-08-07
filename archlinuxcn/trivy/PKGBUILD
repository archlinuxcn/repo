# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=trivy
pkgver=0.10.2
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
sha256sums=('5432a0db7205ef4c642fd7e9bee42daf3d4bf366923da07006b625b015b80f81')

build() {
  cd ${pkgname}-${pkgver}/cmd/trivy
  go build -trimpath -buildmode=pie -mod=readonly -modcacherw -ldflags "-extldflags \"${LDFLAGS}\"" .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm755 cmd/trivy/${pkgname} ${pkgdir}/usr/bin/${pkgname}
}
