# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprogress
_pkgname=fastprogress
pkgver=0.1.21
pkgrel=1
pkgdesc='Simple and flexible progress bar for Jupyter Notebook and console'
arch=('any')
url='https://github.com/dstathis/fastprocess'
license=('Apache')
makedepends=(
  'python-setuptools'
)
source=("https://github.com/fastai/fastprogress/archive/${pkgver}.tar.gz")
sha512sums=('3679629dfe0f64ba3b51ff28b184883e915651f862b06c0494a0956f4fe42110e7e5702d5ea74d99a1a24c0082e90b598ef340c8f960ecde4fb06cb501939bae')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
