# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=3.6.1
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
sha512sums=('a8feaf24251d81c1272c23d059640df37f86e0e5a8de49f9ee7436f985210addca649bb06ce0dd4223c803ad8df2b2a51b829e3fa4397fc22a126a8e0f383679')

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
