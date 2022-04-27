# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=Augmentor
pkgname=python-augmentor
pkgver=0.2.10
pkgrel=1
pkgdesc='Image augmentation library in Python for machine learning'
arch=(any)
url=https://github.com/mdbloice/Augmentor
license=(MIT)
depends=(python-future python-numpy python-pillow python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz"::"https://github.com/mdbloice/Augmentor/archive/${pkgver}.tar.gz")
sha512sums=('19f05014cdaeddcad25f3dca76dfa5bcf6292271ff944322b7b71afb00de863f068b9d4b5b820cf4ab97ba3e4f0a022f85841326494ffac729e9b645d0144fa1')

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
