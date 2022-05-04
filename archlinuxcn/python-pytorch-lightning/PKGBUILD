# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.6.3
pkgrel=1
pkgdesc="The lightweight PyTorch wrapper for high-performance AI research"
arch=('any')
url='https://github.com/PyTorchLightning/pytorch-lightning'
license=('Apache')
depends=(
  python-fsspec
  python-jsonargparse
  python-pandas
  python-pyaml
  python-pydeprecate
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
sha512sums=('0375219a670a45f6f6f729fa401000c71b097ef8bfb66c75ac065d32baa5ad38fc2616245f9cce2198b484c37d1ff3589255af8314b3c5fe983122189924a784')

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
