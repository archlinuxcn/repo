# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.2.1
pkgrel=1
pkgdesc="The lightweight PyTorch wrapper for high-performance AI research"
arch=('any')
url='https://github.com/PyTorchLightning/pytorch-lightning'
license=('Apache')
depends=(
  'python-fsspec'
  'python-pandas'
  'python-pyaml'
  'python-numpy'
  'python-scikit-learn'
  'python-pytorch'
  'python-torchvision'
  'python-twine'
  'python-tqdm'
)
optdepends=(
  'python-apex: mixed precision support'    
  'tensorboard: tensorboard support'
  'python-horovod: for distributed training'
)
makedepends=('python-setuptools')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/PyTorchLightning/pytorch-lightning/archive/${pkgver}.tar.gz")
sha512sums=('9a3166f833b5ce1af19ea25b4343b1a5b294110e62c2bb2c6def71dc053b89211993acf485ffb2520c79fc281cc64b04805d2637f7cc0f11eb40ae7855d9b1bb')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
