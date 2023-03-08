# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-ydata-profiling
_pkgname=ydata-profiling
pkgver=4.1.0
pkgrel=1
pkgdesc='Create HTML profiling reports from pandas DataFrame objects'
arch=('any')
url='https://github.com/ydataai/ydata-profiling'
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
conflicts=(python-pandas-profiling)
replaces=(python-pandas-profiling)
makedepends=(python-setuptools)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ydataai/ydata-profiling/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('564ef188edf85de5cfac605c9dd0bea11034751d4782274db128c14f7419f926c8c41c7973fe126bc869e092218122e99fc1e27a4b2effb11592a637aaa08a26')

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
