# Maintainer: Chad Kunde <Kunde21@gmail.com>

pkgname=gopls
pkgver=0.5.0
pkgrel=0
pkgdesc='Language server for Go programming language'
arch=(x86_64 aarch64 armv7h armv7l)
url='https://github.com/golang/tools/blob/master/gopls'
license=(BSD)
depends=(glibc)
makedepends=('git'
             'go>=1.12')
conflicts=('go-tools'
           'go-tools-complete-git')
provides=('gopls')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/golang/tools/archive/gopls/v${pkgver}.tar.gz")
sha256sums=('1b5f80eb6da71afba18c7d4327d4913cfb9b6a0840ebb33006e3b9eccec12412')

prepare() {
  cd "tools-${pkgname}-v${pkgver}/${pkgname}"

  GOPATH="${srcdir}" GO111MODULE=on go mod download
}

build() {
  cd "tools-${pkgname}-v${pkgver}/${pkgname}"

  GOPATH="${srcdir}" GO111MODULE=on go build -o "../../$pkgname" -trimpath
  GOPATH="${srcdir}" GO111MODULE=on go clean -modcache
  mv ../LICENSE ../../LICENSE
}

package() {
  install -Dm755 "${pkgname}" -t "${pkgdir}"/usr/bin/
  install -Dm644 LICENSE -t ${pkgdir}/usr/share/licenses/${pkgname}/
}

# vim: ts=2 sw=2 et:
