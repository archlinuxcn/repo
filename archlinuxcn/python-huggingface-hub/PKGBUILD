# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.26.3
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
sha512sums=('7bc37c76878cc65a4cfeda16164b3daa118206ffee2acec9bc7be7b020d6f7f44811295f357f05d40d9c4fa37567f1c31ac9643ffc98d8365047db1d32aa44e9')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
