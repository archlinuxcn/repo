# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.26.5
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
sha512sums=('e151e216b681b72ecb28e82d05bb5c6edf25bbbd34d6ce10d2896b54d9fdaf5ec062b2f777a2e5c61fbc92c901351adfb1f9fcfac2efb360e2a3076d5dd08c34')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
