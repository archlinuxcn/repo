# Maintainer: Chad Kunde <Kunde21@gmail.com>

pkgname=gopls
pkgver=0.4.3
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
sha256sums=('b6dfeded6bec0bf960978519cf2d05cb6d996f15d0f13829bdb490de3ca6c675')

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
