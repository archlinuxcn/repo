# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg
pkgname=python-pylibjpeg
pkgver=2.1.0
pkgrel=1
pkgdesc='A Python framework for decoding JPEG images, with a focus on supporting pydicom'
arch=(any)
url='https://github.com/pydicom/pylibjpeg'
license=(MIT)
depends=(
  python-numpy
)
makedepends=(
  python-build
  python-flit-core
  python-installer
  python-wheel
)
optdepends=(
  python-pylibjpeg-libjpeg
  python-pylibjpeg-openjpeg
  python-pylibjpeg-rle
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/pydicom/pylibjpeg/archive/v${pkgver}.tar.gz")
sha512sums=('0aca7112a042a44e39169a38bae27c775765f61d85ef239d6fa4c1bfd75249fddee06a0b590e4011126139df8c737bb27a1e174a84a7cc22195bcc8fd778cce4')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "LICENCE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "${pkgdir}${site_packages}/pylibjpeg/tests"
  rm -rf "${pkgdir}${site_packages}/pylibjpeg/tools/tests"
}
# vim:set ts=2 sw=2 et:
