# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pandas-profiling
_pkgname=pandas-profiling
pkgver=2.11.0
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
sha512sums=('ce73f61df514d650e7d36102fc265915ab991ee93ff83277bea247291842d24929ae7e749f6bdeaf7a3b32b75eb12c760e14841884ab12f3ba1fe1255f45e1bc')

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
