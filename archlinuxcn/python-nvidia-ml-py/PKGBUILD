# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-ml-py
_name=nvidia-ml-py
_pkgname=nvidia_ml_py
pkgver=13.580.65
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
  "${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_pkgname}-${pkgver}.tar.gz"
)
sha512sums=('04202d3df4dff21afe221512f275cd974f9bbe8cf077ec30de79b233f5f3e91eb6a5776aab94e433a36c1bbb6763628f002165fd813bc6d57cc43c37479091eb')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m644 "${srcdir}/${_pkgname}-${pkgver}/README.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
