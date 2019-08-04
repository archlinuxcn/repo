# Maintainer: navigaid <navigaid@gmail.com>
pkgname=yaegi
pkgver=0.0.4
pkgrel=1
pkgdesc='Yaegi is Another Elegant Go Interpreter'
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'aarch64')
url='https://github.com/containous/yaegi'
license=('Apache')
makedepends=()
source=()
sha256sums=()
case "$CARCH" in
  armv5h)
    _pkgarch="armv5"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
  armv6h)
    _pkgarch="armv6"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
  armv7h)
    _pkgarch="armv7"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
  aarch64)
    _pkgarch="arm64"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
  i686)
    _pkgarch="386"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
  x86_64)
    _pkgarch="amd64"
    source+=("${pkgname}-${pkgver}-${_pkgarch}.tar.gz::https://github.com/containous/yaegi/releases/download/v${pkgver}/${pkgname}_v${pkgver}_linux_${_pkgarch}.tar.gz")
    ;;
esac
sha256sums+=('SKIP')

prepare() {
  true
}

build() {
  true
}

package() {
  install -Dm755 yaegi "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
