# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=nipy
pkgname=python-nipy
pkgver=0.6.0
pkgrel=1
pkgdesc='Neuroimaging in Python FMRI analysis package'
arch=('x86_64')
url='http://nipy.org/nipy'
license=('BSD')
depends=(
  python-nibabel
  python-numpy
  python-scipy
  python-sympy
  python-transforms3d
)
makedepends=(
  openblas
  cmake
  cython
  git
  meson-python
  python-build
  python-installer
  python-setuptools
  python-wheel
)
# data files from https://nipy.org/data-packages/
source=(
  'http://nipy.org/data-packages/nipy-templates-0.3.tar.gz'
  'http://nipy.org/data-packages/nipy-data-0.3.tar.gz'
  "${_pkgname}-${pkgver}::git+https://github.com/nipy/nipy.git")
sha512sums=('3af927b8dde0b10ca45899016bce5e4f5b25ef285b2339a63346bfbfa99cc1a0e2f0728336c3ac7e32d4c05375f36fdfa7cf97cdfd26b42834cb3cb631d593b9'
            'ea8ed3537fb00596c16fa8b3464a2da54845ce9782e7bb40eb1157eb94de53892dda99bb4f22a829493cd59cfb47551f39de7641bf65a33678e97e5a4974de1a'
            'SKIP')

prepare() {
  # we don't use ninja from PyPI to build the package
  sed -i "/ninja/d" "${srcdir}/${_pkgname}-${pkgver}/pyproject.toml"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation

  cd "${srcdir}/nipy-data-0.3"
  python -m build --wheel --no-isolation

  cd "${srcdir}/nipy-templates-0.3"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  
  cd "${srcdir}/nipy-data-0.3"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  
  cd "${srcdir}/nipy-templates-0.3"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
