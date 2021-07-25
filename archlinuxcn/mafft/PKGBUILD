# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Steffen Weber <-boenki-gmx-de->
# Contributor: Mick Elliot <micke at sfu dot ca>

pkgname=mafft
pkgver=7.487
pkgrel=1
pkgdesc='Multiple alignment program for amino acid or nucleotide sequences'
arch=('x86_64')
url='https://mafft.cbrc.jp/alignment/software'
license=('BSD')
depends=(
  perl
)
source=("${pkgname}-${pkgver}.tgz::https://mafft.cbrc.jp/alignment/software/${pkgname}-${pkgver}-with-extensions-src.tgz")
sha1sums=('d94137e79ea14c2d235c3f10a6d0537e86768a2e')

build() {
  make -C "${pkgname}-${pkgver}-with-extensions/core" PREFIX=/usr LIBDIR=/usr/lib/mafft
  make -C "${pkgname}-${pkgver}-with-extensions/extensions" PREFIX=/usr LIBDIR=/usr/lib/mafft
}

package() {
  make DESTDIR="${pkgdir}" -C "${pkgname}-${pkgver}-with-extensions/core" install PREFIX=/usr LIBDIR=/usr/lib/mafft
  make DESTDIR="${pkgdir}" -C "${pkgname}-${pkgver}-with-extensions/extensions" install PREFIX=/usr LIBDIR=/usr/lib/mafft
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}-with-extensions/license" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  rm -vf "${pkgdir}/usr/lib/mafft/mafft-homologs.1" "${pkgdir}/usr/lib/mafft/mafft.1"
}
# vim:set ts=2 sw=2 et:
