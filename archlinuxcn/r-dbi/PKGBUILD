# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_cranname=DBI
_cranver=1.1.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="R Database Interface"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(LGPL2.1 LGPL3)
depends=('r>=3.0.0')
optdepends=(r-blob r-covr r-dbplyr r-dplyr r-glue r-hms r-knitr r-magrittr r-rmarkdown r-rprojroot r-rmariadb r-rsqlite r-testthat r-xml2)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('572ab3b8a6421d0ac3e7665c4c842826f1723af98fca25d4f43edb419e771344')

build() {
  cd "${srcdir}"

  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l ${srcdir}
}

package() {
  cd "${srcdir}"

  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
