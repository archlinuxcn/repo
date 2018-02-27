# Maintainer: Dmitri Goutnik <dg@syrec.org>
# Contributor: Sebastian Krebs <sebastian[at]krebs[dot]one>

pkgname=govendor
pkgver=1.0.9
pkgrel=1
pkgdesc='Go vendor tool that works with the standard vendor file.'
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url='https://github.com/kardianos/govendor'
license=('custom:BSD')
depends=('glibc')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('d303abf194838792234a1451c3a1e87885d1b2cd21774867b592c1f7db00551e')

prepare() {
  mkdir -p src/github.com/kardianos
  mv ${pkgname}-${pkgver} src/github.com/kardianos/govendor
}

build() {
  cd src/github.com/kardianos/govendor
  env GOPATH="${srcdir}" go build
}

# check() {
#   cd src/github.com/kardianos/govendor
#   env GOPATH="${srcdir}" go test ./...
# }

package() {
  cd src/github.com/kardianos/govendor
  install -Dm755 govendor "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
