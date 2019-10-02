# Maintainer: herzrasen <dennis.mellert@gmail.com>
pkgname=pkghist
pkgver=0.3.0
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
sha1sums=('855aa995db12e49197fb981e1d58da6d0c8b7439')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cargo build --release
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -D target/release/${pkgname} "${pkgdir}/usr/bin/${pkgname}"
}
