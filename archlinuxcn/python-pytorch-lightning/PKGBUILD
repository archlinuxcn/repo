# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.0.2
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
sha512sums=('1ea6db7656e8987f6212135e49a591fcc56bab23a362716716c0a71227aedb937a517988be1247de672d308996c2a7a38ce32f28d7758eccd034462bbb281f86')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
