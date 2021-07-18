# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagehash
_pkgname=imagehash
pkgver=4.2.1
pkgrel=1
pkgdesc='A Python Perceptual Image Hashing Module'
arch=('any')
url='https://github.com/JohannesBuchner/imagehash'
license=('BSD')
depends=(
  python-numpy
  python-pillow
  python-pywavelets
  python-scipy
  python-six
)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/JohannesBuchner/imagehash/archive/v${pkgver}.tar.gz"
)
sha512sums=('420987beee8665d2bc3455cf1d1dd6b4b471ba02a1b14f7feb0a9324db54ba0d308341f46bf49caa87a9c84ebc9a2d9cec0dfb40dfb0eb75f70a6d42e523dcef')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  rm -rfv "${pkgdir}/usr/images"
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
