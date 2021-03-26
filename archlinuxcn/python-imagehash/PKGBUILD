# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagehash
_pkgname=imagehash
pkgver=4.1.0
pkgrel=2
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
  "0001-fix-version-formatting.patch::https://github.com/JohannesBuchner/imagehash/commit/acf912939ac7d03b54ada44798afd820c64142a1.patch"
)
sha512sums=('a656a476d389f59ec722603abb24962f6b0aad726c8429dc4aeccce4656cc81406aa70ca23f0118251b588df18da4c0e2c1cc7a9d29640dcf3c47df5910f9624'
            '4958bcc55c2d062479e42ed7a0216fd9fce6be32f4bc0a08c93f2b16d0a0a04cfc2088c9f687ab9e61cd1499dc49b809755bb09edaedf8811f45a7b47f3bff9a')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-version-formatting.patch"
}

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
