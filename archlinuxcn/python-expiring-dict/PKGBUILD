# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=expiring-dict
_name=expiring_dict
pkgname=python-expiring-dict
pkgver=1.1.2
pkgrel=1
pkgdesc='Python dict with TTL support for auto-expiring caches'
arch=('any')
url='https://pypi.org/project/expiring-dict'
license=('MIT')
depends=(
  python-sortedcontainers
)
makedepends=(
  python-build
  python-setuptools
  python-installer
  python-wheel
)
source=("${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_pkgname}/${_name}-${pkgver}.tar.gz"
        "https://github.com/dparker2/py-expiring-dict/raw/master/LICENSE"
)
sha512sums=('a5f768a9317723284b7deb9c592f3562e62d314be6649c9b198d9dafbcf3fab357d610fe87583439d6de77d6a59b88863409c453f08de4b06a30c06a64d38bd5'
            '10febcc48b9f8d7210144cf00edbac8b82482f7ebefb0a1af05125fb3672acff765499f1627f9b80afe24cc926751b104e205b48a414c92c28d9c2d2b7c99814')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
