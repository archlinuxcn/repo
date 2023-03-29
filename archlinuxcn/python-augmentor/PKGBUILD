# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=Augmentor
pkgname=python-augmentor
pkgver=0.2.12
pkgrel=1
pkgdesc='Image augmentation library in Python for machine learning'
arch=(any)
url=https://github.com/mdbloice/Augmentor
license=(MIT)
depends=(python-future python-numpy python-pillow python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz"::"https://github.com/mdbloice/Augmentor/archive/${pkgver}.tar.gz")
sha512sums=('27a37d52cbf51dcb2bb8c7c5d74efbe2d2cb066b9ed958b3a84456d524fff82dd19e9da1ab23064490171d078ebd764e900fc39d8fb4e4bd1e23b13e0589cb85')

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
