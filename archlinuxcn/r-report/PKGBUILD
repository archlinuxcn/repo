# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=report
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=2
pkgdesc='Automated Reporting of Results and Statistical Models'
arch=('any')
url="https://github.com/easystats/report"
license=('GPL')
depends=(
  r
  r-bayestestr
  r-datawizard
  r-effectsize
  r-insight
  r-parameters
  r-performance
)
optdepends=(
  r-bayesfactor
  r-brms
  r-dplyr
  r-httr
  r-knitr
  r-lavaan
  r-lme4
  r-logspline
  r-rmarkdown
  r-rstanarm
  r-spelling
  r-testthat
)
source=("${_pkgname}_${pkgver}.tar.gz::https://github.com/easystats/report/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c661f4682cfa03936052fea733043f255b31d653ce3280006adffbc9f48b05fd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
