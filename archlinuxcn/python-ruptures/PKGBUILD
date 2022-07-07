# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=ruptures
pkgname=python-ruptures
pkgver=1.1.7
pkgrel=1
pkgdesc='Change point detection in Python'
arch=('x86_64')
url='https://github.com/deepcharles/ruptures'
license=('BSD')
depends=(
  python-scipy
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)
checkdepends=(
  python-pytest
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/deepcharles/ruptures/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('8445f7c1a211c16adab7008ab779aa9206214b4db33c8a975126ad5df98c594ed1fab9a000b457d56593d0005f0479886578358c295559cd81b6752cc20cd64b')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib.linux-${CARCH}-$(get_pyver)" pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
