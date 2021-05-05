# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=2.12.0
pkgrel=1
pkgdesc='Create HTML profiling reports from pandas DataFrame objects'
arch=('any')
url='https://github.com/pandas-profiling/pandas-profiling'
license=('MIT')
depends=(
  python-attrs
  python-confuse
  python-htmlmin
  python-ipywidgets
  python-jinja
  python-joblib
  python-matplotlib
  python-missingno
  python-numpy
  python-pandas
  python-phik
  python-requests
  python-seaborn
  python-scipy
  python-tangled-up-in-unicode
  python-tqdm
  python-visions
)

makedepends=(python-setuptools)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pandas-profiling/pandas-profiling/archive/v${pkgver}.tar.gz")
sha512sums=('604568573528571cbaf5b2fbb2d7263d73ec84ee7aa301061668fd1aefb2e6527c12b881a8bcab1e85ae7480799891205d7227961d04279115588fcbbea1ab6f')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
