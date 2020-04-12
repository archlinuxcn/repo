# Maintainer: Hao Long <aur@esd.cc>

pkgname=gowitness
pkgver=1.3.3
pkgrel=1
pkgdesc="a golang, web screenshot utility using Chrome Headless"
arch=("x86_64" "i686")
url="https://github.com/sensepost/gowitness"
license=("GPL3")
depends=("chromium")
makedepends=("go-pie")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('5e9af404e8a54b8996f15bbad442645c56c88423250ab72698d6cced8cdac7b1')

build() {
  cd ${pkgname}-${pkgver}
  go build -trimpath -ldflags "-extldflags ${LDFLAGS}" .
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  install -Dm755 gowitness ${pkgdir}/usr/bin/${pkgname}
}
