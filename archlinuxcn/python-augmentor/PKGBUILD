# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=Augmentor
pkgname=python-augmentor
pkgver=0.2.7
pkgrel=1
pkgdesc='Image augmentation library in Python for machine learning'
arch=(any)
url=https://github.com/mdbloice/Augmentor
license=(MIT)
depends=(python-future python-numpy python-pillow python-tqdm)
makedepends=(python-setuptools)
checkdepends=(python-pytest)
source=("${_pkgname}-${pkgver}.tar.gz"::"https://github.com/mdbloice/Augmentor/archive/${pkgver}.tar.gz")
sha512sums=('a9ef1371b2b585e78ac9690c9f145a97b80b450e08b101b04a59020a545cbb9a9bb727ab711e0181d25845d2212b8ae80d6076da81b28bf9c28c9ae23ff5fe6b')

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
