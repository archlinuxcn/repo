# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: pingplug < aur at pingplug dot me >

_pkgname=openslide-python
pkgname=python-openslide
pkgver=1.1.2
pkgrel=2
pkgdesc='Python bindings to OpenSlide'
arch=('x86_64')
url='https://github.com/openslide/openslide-python'
license=('LGPL')
makedepends=(python-setuptools)
checkdepends=(python-pytest)
depends=(
  openslide
  python-pillow
)
source=(
  "${_pkgname}-${pkgver}.tar.gz::https://github.com/openslide/openslide-python/archive/v${pkgver}.tar.gz"
)
sha256sums=('83e064ab4a29658e7ddf86bf1d3e54d2508cc19ece35d55b55519c826e45d83f')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build_ext --inplace
  python setup.py build
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
