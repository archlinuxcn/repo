# Maintainer: 2ion
pkgname=advancecomp
pkgver=2.1
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc="Recompression utilities for .zip .png .mng and .gz files using the 7-zip algorithm"
url='http://www.advancemame.it/'
license=('GPL')
depends=('zlib' 'gcc-libs')
makedepends=()
source=("https://github.com/amadvance/advancecomp/releases/download/v${pkgver}/advancecomp-${pkgver}.tar.gz")
sha256sums=('3ac0875e86a8517011976f04107186d5c60d434954078bc502ee731480933eb8')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -Dm644 HISTORY "$pkgdir"/usr/share/doc/advancecomp/HISTORY
}
