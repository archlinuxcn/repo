# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagehash
_pkgname=imagehash
pkgver=4.3.0
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
sha512sums=('a8100518bd6c312e6feeaeb6a2c2bf793e285d7b96585cffec1be32ae04b1ba6546583ba99ea8fa16a1646a03dd375d50ed82f3daa5edf3c0c4eaf0c1644289b')

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
