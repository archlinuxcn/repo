# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=3.6.3
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
sha512sums=('f81891786bfc655b6bc42aa1d67703a6f3b528373b82feaa85d810beb841b73d523f403a27a03c5f6ea8b8ba4b91b9e30b0eaa949af6fe2504fbbe82579f5878')

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
