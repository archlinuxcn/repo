# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.4.1
pkgrel=1
pkgdesc="The lightweight PyTorch wrapper for high-performance AI research"
arch=('any')
url='https://github.com/PyTorchLightning/pytorch-lightning'
license=('Apache')
depends=(
  python-fsspec
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
sha512sums=('7f81f7772ba8573e0aa97b4d4b9df91fb5fd14ee91b864a48ba7e9480f72b786cfeff04f80cb74e082a1467580e42b645b426981e5a068eeb4d7b5f06f22d485')

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
