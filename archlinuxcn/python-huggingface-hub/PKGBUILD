# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.26.0
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
sha512sums=('c30cca2b679fe48168dc379b52bcd9a9781be6533f68016a3ff7707fff0826ce42d06339787c1a754c75397d53815eab3eb402978577de9ec1d4dcfa976c7746')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
