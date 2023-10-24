# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-ydata-profiling
_pkgname=ydata-profiling
pkgver=4.6.1
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
sha512sums=('d4a95497a52f9631550b2ca2942f1c96d70c4879b30c29c5d05a0772c4dd1d7e72faf1554046e0d18d077afbca660355e1b9d386c6dedfac0422afb2cf25353c')

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
