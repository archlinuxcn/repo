# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-ml-py
_name=nvidia-ml-py
pkgver=12.555.43
pkgrel=1
pkgdesc='Python Bindings for the NVIDIA Management Library'
arch=('any')
url='https://pypi.org/project/nvidia-ml-py'
license=('BSD-3-Clause')
depends=(
  nvidia-utils
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=(
  "${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
)
sha512sums=('11ff0d437594567d978a2165bc93c494abc0317503a7026907242903f79b426dd7568819218a3a3cd7d9d41d110aa4555d10e4d7a3ad971fe4134820752326fd')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m644 "${srcdir}/${_name}-${pkgver}/README.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
