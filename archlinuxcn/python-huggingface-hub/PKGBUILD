# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.25.2
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
sha512sums=('8933e469cd1e8fc43e9da3991f6acb598531c01bcd833218a1838419774d613102c095ce3beebab8dae1ff2708946d8f417b9861c69a460d38eae24f9bb9d718')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
