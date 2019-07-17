# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=Augmentor
pkgname=python-augmentor
pkgver=0.2.6
pkgrel=1
pkgdesc='Image augmentation library in Python for machine learning'
arch=(any)
url=https://github.com/mdbloice/Augmentor
license=(MIT)
depends=(python-future python-numpy python-pillow python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz"::"https://github.com/mdbloice/Augmentor/archive/${pkgver}.tar.gz")
sha512sums=('e4f7416dad429c7f16a0b4b68b3998482d8ff4b7ece91b9812ac4cbaad81d946fe6c1c8eed2ad2d7c7353f389938bc72c745f18f2dd818f17f64e05063985d71')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
