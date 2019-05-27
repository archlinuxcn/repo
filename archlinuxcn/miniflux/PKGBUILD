# Maintainer: Clar Charr <clar@charr.xyz>

pkgname=miniflux
pkgver=2.0.15
pkgrel=4
pkgdesc='Minimalist Feed Reader'
arch=('x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url='https://miniflux.app'
license=('Apache')
depends=('postgresql')
makedepends=('go' 'godep' 'git')
conflicts=('miniflux-git')
backup=('etc/miniflux.conf')
source=(
  https://github.com/miniflux/miniflux/archive/${pkgver}.tar.gz
  miniflux.conf
  miniflux.service
  miniflux.sysusers
)
sha256sums=(
  '02500db5655754116379b92acb11b3b040bcb9ba707014f74e0cc21dfdcbd0ff'
  '1247a3cfe0307f5f1bb070e616f57344d8f16201070ecf7dda243b3fa1fbd8b8'
  '2b3b50d9b50581a80e85e23011c8b5dd048247206083615f213d63b70f8f13be'
  'd1ce5acf1e633b04b92bf9330bd64d97c19d8f8d39c7bb4b64e11a96be4b73e2'
)

prepare() {
  mkdir -p "${srcdir}/src/github.com/miniflux"
  ln -s "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/github.com/miniflux/${pkgname}"
}

case "$CARCH" in
  x86_64) _target=amd64 ;;
  i686) _target=x86 ;;
  arm) _target=armv5 ;;
  armv6h) _target=armv6 ;;
  armv7h) _target=armv7 ;;
  aarch64) _target=armv8 ;;
  *) return 1 ;;
esac

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin/" make linux-$_target
}

package() {
  install -Dm644 "${srcdir}/miniflux.conf" "${pkgdir}/etc/miniflux.conf"
  install -Dm644 "${srcdir}/miniflux.service" "${pkgdir}/usr/lib/systemd/system/miniflux.service"
  install -Dm644 "${srcdir}/miniflux.sysusers" "${pkgdir}/usr/lib/sysusers.d/miniflux.conf"
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/miniflux-linux-${_target}" "${pkgdir}/usr/bin/miniflux"
}

