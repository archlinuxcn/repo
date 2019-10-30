# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>

_reponame=dell-bios-fan-control
pkgname=dell-bios-fan-control-git
pkgver=r3.a2c81a2
pkgrel=1
pkgdesc="A user space utility to set control of fans by bios on some Dell XPS Laptops."
arch=('i686' 'x86_64')
url="https://github.com/TomFreudenberg/dell-bios-fan-control"
license=('GPL2')
depends=('glibc')
optdepends=('i8kutils: to control Dell laptop system temperature')
makedepends=('git')
conflicts=()
provides=()
source=('git+https://github.com/TomFreudenberg/dell-bios-fan-control.git'
  'dell-bios-fan-control.service')
sha256sums=('SKIP'
  'c090e883d8aa4942cb6f4d9c2aeaa353f7c49ec83a0fa0fc404bceafb42e4ab0')

pkgver() {
  cd "${srcdir}/${_reponame}"
  ( set -o pipefail
  git describe --long 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' \
  || printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

build() {
  cd "${_reponame}"
  make
}

package() {
  cd "${_reponame}"
  install -D -m755 dell-bios-fan-control "${pkgdir}/usr/bin/dell-bios-fan-control"
  install -D -m644 ../dell-bios-fan-control.service "${pkgdir}/usr/lib/systemd/system/dell-bios-fan-control.service"
}
