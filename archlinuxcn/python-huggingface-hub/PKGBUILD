# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=huggingface_hub
pkgname=python-huggingface-hub
pkgver=0.4.0
pkgrel=1
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
sha512sums=('f937c013f3fe84b1ff456b495edd93ba557b242cc8ff10005b1b52648508b162a07f5a4bc628b88a206fa605c6d56481dd98d3650c42d727daff96fc3c9c4d07')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
