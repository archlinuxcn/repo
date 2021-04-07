# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.2.7
pkgrel=1
pkgdesc="The lightweight PyTorch wrapper for high-performance AI research"
arch=('any')
url='https://github.com/PyTorchLightning/pytorch-lightning'
license=('Apache')
depends=(
  python-fsspec
  python-pandas
  python-pyaml
  python-numpy
  python-scikit-learn
  python-pytorch
  python-torchmetrics
  python-torchvision
  python-twine
  python-tqdm
  tensorboard
)
optdepends=(
  'python-apex: mixed precision support'    
  'python-horovod: for distributed training'
)
makedepends=('python-setuptools')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/PyTorchLightning/pytorch-lightning/archive/${pkgver}.tar.gz")
sha512sums=('2c980861b307c6e8364e96947db890ee2528293278c0e7b5e00ae79ed804fdd6661a54962acbb16809ac926286ebcdbf5377a8bdc82ae399f9dd8a92f14e2289')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
