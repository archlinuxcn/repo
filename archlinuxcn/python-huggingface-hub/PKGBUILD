# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.13.3
pkgrel=1
epoch=1
pkgdesc='All the open source things related to the Hugging Face Hub'
arch=('any')
url='https://github.com/huggingface/huggingface_hub'
license=('Apache')
depends=(
  python-filelock
  python-requests
  python-tqdm
  python-yaml
  python-typing_extensions
  python-packaging
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/huggingface/huggingface_hub/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b611c3048368c539820ec0dfe26cfa88b32fefdcc2460101284dc4caac29b3dd2a762628ab58212083d3219f7129c2544db6123cadbef75b362ecba706734414')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
