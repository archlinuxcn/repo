# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=2.13.0
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
sha512sums=('53dd9c29b100a8ebf8e4db05e2dd07edfc43ffeae7aabdd34abd3daef14cd6dac3a3d229576747d534c7f218e562e3a159a5c854824f8c15ec84df359f12b4f4')

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
