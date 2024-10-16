# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-ydata-profiling
_pkgname=ydata-profiling
pkgver=4.11.0
pkgrel=1
pkgdesc='Create HTML profiling reports from pandas DataFrame objects'
arch=('any')
url='https://github.com/ydataai/ydata-profiling'
license=('MIT')
depends=(
  ipython
  python-dacite
  python-dateutil
  python-htmlmin
  python-imagehash
  python-ipywidgets
  python-jinja
  python-joblib
  python-matplotlib
  python-markupsafe
  python-missingno
  python-multimethod
  python-networkx
  python-numba
  python-numpy
  python-pandas
  python-phik
  python-pillow
  python-pydantic
  python-requests
  python-seaborn
  python-scipy
  python-statsmodels
  python-tangled-up-in-unicode
  python-tqdm
  python-typeguard
  python-visions
  python-wordcloud
  python-yaml
)
conflicts=(python-pandas-profiling)
replaces=(python-pandas-profiling)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ydataai/ydata-profiling/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('2ca212e5aadd34738b2058f1ea3845c35262bbc49f9e7a39b71557f68ece3199d50b9ac084a551d1be6fc4a7f8d6ba8c8944d87a376e975e9ea0b93cd52af549')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
