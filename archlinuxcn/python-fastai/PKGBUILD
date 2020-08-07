# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastai
_pkgname=fastai
pkgver=1.0.63
pkgrel=1
pkgdesc='Deep learning library build on PyTorch'
arch=('any')
url='https://github.com/fastai/fastai'
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/fastai/fastai/archive/${pkgver}.tar.gz")
sha512sums=('76dc765ffd88c82c0df7f915a3c190b3c1e13ea3f533bf9edf7e4f240ac4e662fda63b318cb05b40ed1dcfe94391ba72c72097b664e1efab9c18d6b51bd084cb')

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
