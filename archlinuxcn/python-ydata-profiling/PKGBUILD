# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-ydata-profiling
_pkgname=ydata-profiling
pkgver=4.4.0
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
sha512sums=('6bc3550d57f3d685e976cc4ec521a243ab81aebcecfcc704bc78aab11671f0720ac847d23a817e631d5dd3bcbc1b5d2d7ade2acc980b776bc1e89197e5d7b479')

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
