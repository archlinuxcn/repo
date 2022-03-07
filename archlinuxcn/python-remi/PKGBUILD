# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=remi
pkgname=python-remi
pkgver=2022.03.07
pkgrel=1
pkgdesc='Cross-platform GUI library which renders in a web browser'
arch=('any')
url='https://github.com/dddomodossola/remi'
license=('Apache')
depends=(
  python
)
makedepends=(
  python-setuptools
)
optdepends=(
  'python-pywebview: for standalone app'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dddomodossola/remi/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('81965937ac80599b7342af6ec57c415b962b2e629fe733b6759e8f4d7d7e9667')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/test"
  mkdir -p "${pkgdir}/usr/share/doc/${pkgname}"
  mv -vf "examples" "${pkgdir}/usr/share/doc/${pkgname}"
}
# vim:set ts=2 sw=2 et:
