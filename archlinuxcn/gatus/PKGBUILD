# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=gatus
pkgver=5.35.0
pkgrel=1
pkgdesc="Automated service health dashboard"
arch=("x86_64")
url="https://github.com/TwiN/gatus"
license=("Apache-2.0")
backup=('etc/gatus.yaml')
depends=("glibc")
makedepends=("go")
source=('gatus.service'
        'sysusers.conf'
        'tmpfiles.conf'
        "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('4ec6761e07afe08137d28ba38c208e6a6717c4943cea62fb732ce83cab7fa9455ac39ab2faab83a8f6554fbdc8443d99c4d400291d90dbe778e86a2c022e3f67'
        'a1818c1b4ff769285ea1eb3fcede9da445f0abbed0583d1817107b2b2798924559fac0b5e7a658a910c15a6bbf33f2fab4019e43e158eebf11b668a3af5f0a82'
        '29a8c9b50852dcb04c8e67b80d9a48d4d303caa9dfcae54fdb5026417752f11a4fe594fbe4f535527cc7e05201b442ac92f63cdee789de5bce9246cc8e102506'
        '5c50c0bd9e5a317f8590c520aae363152a655fef1889731a11cbe9a3190f2d34238c516f0e30b89035af659171fd35f991b625d9c90421f8109e1e04b31dcc14')

prepare() {
  cd "${pkgname}-${pkgver}"
  export GOPATH="${srcdir}"
  go mod download -modcacherw
}

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
  install -Dm644 "${srcdir}/sysusers.conf" "${pkgdir}/usr/lib/sysusers.d/gatus.conf"
  install -Dm644 "${srcdir}/tmpfiles.conf" "${pkgdir}/usr/lib/tmpfiles.d/gatus.conf"
}
