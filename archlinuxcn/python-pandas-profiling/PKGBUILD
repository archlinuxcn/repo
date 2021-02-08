# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=2.10.1
pkgrel=1
pkgdesc='Create HTML profiling reports from pandas DataFrame objects'
arch=('any')
url='https://github.com/pandas-profiling/pandas-profiling'
license=('MIT')
depends=(
#  python-astropy
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
  python-requests
  python-seaborn
  python-scipy
  python-tangled-up-in-unicode
  python-tqdm
  python-visions
)

makedepends=(python-setuptools)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/pandas-profiling/pandas-profiling/archive/v${pkgver}.tar.gz")
sha512sums=('5bf67b00d8e2921c3184a52ad6221089c9ce8bae6edbf246c63ca6f090c3447fe8112f1bdde05a8ff0519bd864b9e9548259b7900dc31cd930769e7cc3d4f233')

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
