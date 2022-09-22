# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pytorch-lightning
_pkgname=pytorch-lightning
pkgver=1.7.7
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
sha512sums=('7025d0f68768155190bcabaa3d49e6ae50af7a926c5774b652c6799c48e8e832edc0de29401b625e3369d033ed2f3b4466a5f41ee0f3c90554be6b28b3edc79f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
