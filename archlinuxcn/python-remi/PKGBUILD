# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=remi
pkgname=python-remi
pkgver=2022.7.27
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
sha256sums=('362375d60e4e460a88c9f2198a83ae7a6476a32987d2fc97154211be829331f5')

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
