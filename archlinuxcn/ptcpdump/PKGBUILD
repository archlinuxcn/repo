# Maintainer: poscat
pkgname=ptcpdump
pkgver=0.37.1
pkgrel=1
pkgdesc='packet capture tool with process awareness'
arch=('x86_64' 'aarach64')
url='https://github.com/mozillazg/ptcpdump'
license=('MIT')
depends=('libpcap' 'glibc')
makedepends=('go')
source=("ptcpdump-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('6c90314ef1420e87fa1ca5f76ed7832063675a2ad6ef722cdd4eeeb9e4246c81')

build() {
  cd "${srcdir}"/ptcpdump-${pkgver}
  go build \
    -tags dynamic \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -trimpath \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\""
}

package() {
  cd "${srcdir}"/ptcpdump-${pkgver}
  install -Dvm755 -t "${pkgdir}"/usr/bin ptcpdump
  install -Dvm644 -t "${pkgdir}"/usr/share/licenses/${pkgname} LICENSE
}
