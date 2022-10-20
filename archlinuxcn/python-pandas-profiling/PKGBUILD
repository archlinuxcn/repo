# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=3.4.0
pkgrel=1
pkgdesc='Create HTML profiling reports from pandas DataFrame objects'
arch=('any')
url='https://github.com/ydataai/pandas-profiling'
license=('MIT')
depends=(
  python-htmlmin
  python-imagehash
  python-ipywidgets
  python-jinja
  python-joblib
  python-matplotlib
  python-missingno
  python-multimethod
  python-numpy
  python-pandas
  python-phik
  python-pydantic
  python-requests
  python-seaborn
  python-scipy
  python-statsmodels
  python-tangled-up-in-unicode
  python-tqdm
  python-visions
  python-yaml
)

makedepends=(python-setuptools)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pandas-profiling/pandas-profiling/archive/v${pkgver}.tar.gz")
sha512sums=('a51b553658f41a594a4b868a663345649a60076cdc38bec595f20d942892cce3ea766d487c56f600ae2092abb3dcb90be6d5fd59b386307920f4e30f5ba09e46')

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
