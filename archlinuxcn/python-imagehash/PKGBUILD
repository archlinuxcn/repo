# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagehash
_pkgname=imagehash
pkgver=4.3.2
pkgrel=1
pkgdesc='A Python Perceptual Image Hashing Module'
arch=('any')
url='https://github.com/JohannesBuchner/imagehash'
license=('BSD-3-Clause')
depends=(
  python-numpy
  python-pillow
  python-pywavelets
  python-scipy
  python-six
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/JohannesBuchner/imagehash/archive/v${pkgver}.tar.gz"
)
sha512sums=('9071e93e71903d0695ece879462acd45b3ae07a962c72816149a5af3d7fcb56330b208f9dcea6ad177e0efcfe3c5574479e5eda6b2d5f4b2f6453098c11d8f70')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  rm -rfv "${pkgdir}/usr/images"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
