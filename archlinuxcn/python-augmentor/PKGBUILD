# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=Augmentor
pkgname=python-augmentor
pkgver=0.2.8
pkgrel=1
pkgdesc='Image augmentation library in Python for machine learning'
arch=(any)
url=https://github.com/mdbloice/Augmentor
license=(MIT)
depends=(python-future python-numpy python-pillow python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz"::"https://github.com/mdbloice/Augmentor/archive/${pkgver}.tar.gz")
sha512sums=('58bd6d2d8f13cb4e0198bf49f6f6586d8b05c455f2552aa5e7ae0fa0d6f974333d1c084ae9771acd4e59b023fc00d8b10bcc987af7012194f43a7c4fbf35a8d2')

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
