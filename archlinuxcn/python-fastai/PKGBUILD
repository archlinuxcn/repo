# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastai
_pkgname=fastai1
pkgver=1.0.63
pkgrel=2
pkgdesc='Deep learning library build on PyTorch (legacy v1 release)'
arch=('any')
url='https://github.com/fastai/fastai1'
license=('BSD')
depends=(
  python-beautifulsoup4
  python-bottleneck
  python-fastprogress
  python-matplotlib
  python-numexpr
  python-numpy
  python-nvidia-ml-py3
  python-packaging
  python-pandas
  python-pillow
  python-pyaml
  python-pytorch
  python-scikit-image
  python-scipy
  python-torchvision
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/fastai/fastai1/archive/${pkgver}.tar.gz")
sha512sums=('711b2007199192cf9d8495a8c7c2cc084a2ab62ab40765bc1963be8bc23b154ab4874bf8204535b345db3c3c57912808126d142de6f5b19bde2a7f4e44271de3')

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
