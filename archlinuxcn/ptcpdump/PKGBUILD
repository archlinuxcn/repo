# Maintainer: poscat
pkgname=ptcpdump
pkgver=0.37.2
pkgrel=1
pkgdesc='packet capture tool with process awareness'
arch=('x86_64' 'aarach64')
url='https://github.com/mozillazg/ptcpdump'
license=('MIT')
depends=('libpcap' 'glibc')
makedepends=('go')
source=("ptcpdump-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('ce48c34dba6d92ae05bb63c9e2c474bcd6cdb4140831472bc41e36fc61f199f8')

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
