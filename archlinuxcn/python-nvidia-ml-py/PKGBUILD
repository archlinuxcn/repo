# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-ml-py
_name=nvidia-ml-py
_pkgname=nvidia_ml_py
pkgver=12.570.86
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
sha512sums=('83585ca3e275fa6f7008966522eb8b61ceb6f340ec21168cf72448d66660340eb263b47f1ad7ef14811390fe8e5a5bfe0a3c275bca9d240f5872861c86f8b083')

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
