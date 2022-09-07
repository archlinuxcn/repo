# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.7.5
pkgrel=1
pkgdesc="The lightweight PyTorch wrapper for high-performance AI research"
arch=('any')
url='https://lightning.ai'
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
makedepends=(
  python-build
  python-installer
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('1c59c57474337dfbd2cf42ed60c5720c0a9ce92a40fee3ee6d5aa9e269f510411a151d13840b383d5b51c4398968582631ab5f8a05d632909d1deb7168b76686')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
