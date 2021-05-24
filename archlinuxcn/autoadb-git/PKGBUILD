# Maintainer: Cullen Ross <cullenrss@gmail.com>

_pkgname='autoadb'
pkgname="${_pkgname}-git"
pkgver=r4.7f84029
pkgrel=3
arch=('any')
license=('Apache')
makedepends=('git' 'rust' 'curl')
provides=('autoadb')
conflicts=('autoadb')
pkgdesc="Allows executing a command whenever a new device is connected to adb"
url="https://github.com/rom1v/${_pkgname}"
source=("git+https://github.com/rom1v/autoadb")
sha256sums=('SKIP')

pkgver() {
  cd "${_pkgname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd $srcdir/${_pkgname}
  curl http://www.apache.org/licenses/LICENSE-2.0 > LICENSE
  sed -i '190s/.*/   Copyright (C) 2017 Genymobile\n   Copyright (C) 2019 Romain Vimont/' LICENSE
  cargo build --release
}

package() {
  cd $srcdir/${_pkgname}
  install -D -m 755 "$srcdir/${_pkgname}/target/release/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/${_pkgname}"
}
