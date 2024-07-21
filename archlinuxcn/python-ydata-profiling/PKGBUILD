# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-ydata-profiling
_pkgname=ydata-profiling
pkgver=4.9.0
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
sha512sums=('68585709f150a090e72d3c992a5192627c4f281fb2e5022ec4e17977019dea27967cb7396fec648ea3ed2857395e568afbe748fb1979c463fbb10e1af6f35d21')

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
