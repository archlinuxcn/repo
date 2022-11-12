# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

pkgname=gatus
pkgver=4.3.2
pkgrel=1
pkgdesc="Automated service health dashboard"
arch=("x86_64")
url="https://github.com/TwiN/gatus"
license=("Apache")
backup=('etc/gatus.yaml')
depends=("glibc")
makedepends=("go")
source=('gatus.service'
        'sysusers.d'
        "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('fdcd8d6efef5c4057ad2944c4392d15474d5c40e6494399f028a37863cfe905a2ee2bb484259987fb6ae72035e2fddafde8f7209c8b6fa8897b41393f60004bb'
        'fa96208d814d389bf885c9f224b4c7093566fd36901016df915a09e26db6227a65af528674204a73e8bbba5aa5ea24862f0bee2930e2687fbc77166e78395dc6'
        '669f3594108e0c3ea16229ccb1ac3b19b201340a5a55adf3d27a04be334f0048036f4b007aeaa47ead31e95bdfacd40b31d3b56f55003bc5a634fb766e11dcf7')

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
