# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.26.1
pkgrel=1
epoch=1
pkgdesc='All the open source things related to the Hugging Face Hub'
arch=('any')
url='https://github.com/huggingface/huggingface_hub'
license=('Apache-2.0')
depends=(
  python-aiohttp
  python-fastapi
  python-fsspec
  python-filelock
  python-numpy
  python-packaging
  python-pydantic
  python-requests
  python-tqdm
  python-yaml
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  python-graphviz
  python-hf-transfer
  python-inquirerpy
  python-minijinja
  python-pydot
  python-pytorch
  python-safetensors
  python-tensorflow
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/huggingface/huggingface_hub/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('463d99eac8fa0c96584b285b83afec0a8452704e28155377235ec03111ff1775721abe624a8b83861c9077eca1c3030c33a07be9e63c311189e5d8bd99edcdfd')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
