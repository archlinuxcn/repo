# Maintainer: herzrasen <dennis.mellert@gmail.com>
pkgname=pkghist
pkgver=0.2.0
pkgrel=1
pkgdesc="Query your pacman logs"
arch=('x86_64')
url="https://github.com/herzrasen/pkghist"
license=('MIT')
makedepends=(
  'git'
  'rust'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/herzrasen/pkghist/archive/v${pkgver}.tar.gz")
sha1sums=('07e3e882a8102170c3ce5595355665d13425967e')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -D target/release/${pkgname} "${pkgdir}/usr/bin/${pkgname}"
}
