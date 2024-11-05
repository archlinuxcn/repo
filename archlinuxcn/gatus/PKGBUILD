# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=gatus
pkgver=5.13.1
pkgrel=1
pkgdesc="Automated service health dashboard"
arch=("x86_64")
url="https://github.com/TwiN/gatus"
license=("Apache-2.0")
backup=('etc/gatus.yaml')
depends=("glibc")
makedepends=("go")
source=('gatus.service'
  'sysusers.d'
  "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('4ec6761e07afe08137d28ba38c208e6a6717c4943cea62fb732ce83cab7fa9455ac39ab2faab83a8f6554fbdc8443d99c4d400291d90dbe778e86a2c022e3f67'
        'a1818c1b4ff769285ea1eb3fcede9da445f0abbed0583d1817107b2b2798924559fac0b5e7a658a910c15a6bbf33f2fab4019e43e158eebf11b668a3af5f0a82'
        '568f3f5a8bd80029c03418a118079853becd2cff316c8f31619986950eb22c427399f708c194d162e660c8612125ec41f1cf4a7b80111d033fa11c560a2362dc')

build() {
  cd "${pkgname}-${pkgver}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build .
}

package() {
  cd "${pkgname}-${pkgver}"
  install -Dm755 gatus "${pkgdir}/usr/bin/gatus"
  install -Dm644 config.yaml "${pkgdir}/etc/gatus.yaml"
  install -Dm644 "${srcdir}/gatus.service" "${pkgdir}/usr/lib/systemd/system/gatus.service"
  install -Dm644 "${srcdir}/sysusers.d" "${pkgdir}/usr/lib/sysusers.d/gatus.conf"
}
