# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>

_reponame=dell-bios-fan-control
pkgname=dell-bios-fan-control-git
pkgver=r5.2700610
pkgrel=5
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
  'dell-bios-fan-control.service'
  'dell-bios-fan-control-resume.service')
sha256sums=('SKIP'
            '0a7e12c6c720be14411654b934a7b045a121510079f42788f30af06cedd659c6'
            '58216810f57ab7574d017451396f132c61c805bba46565b982385c73a479cd9f')

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
  install -D -m644 ../dell-bios-fan-control-resume.service "${pkgdir}/usr/lib/systemd/system/dell-bios-fan-control-resume.service"
}
