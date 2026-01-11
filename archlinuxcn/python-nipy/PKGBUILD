# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=nipy
pkgname=python-nipy
pkgver=0.6.1
pkgrel=3
pkgdesc='Neuroimaging in Python FMRI analysis package'
arch=('x86_64')
url='http://nipy.org/nipy'
license=('BSD-3-Clause')
depends=(
  openblas
  python-nibabel
  python-numpy
  python-scipy
  python-sympy
  python-transforms3d
)
makedepends=(
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
  "https://github.com/nipy/nipy/pull/589.patch"
  'http://nipy.org/data-packages/nipy-templates-0.3.tar.gz'
  'http://nipy.org/data-packages/nipy-data-0.3.tar.gz'
  "${_pkgname}-${pkgver}::git+https://github.com/nipy/nipy.git")
sha512sums=('e01b353a6535e4f5fb4c968aad8e2f7c6111c8323f41d129645af51780307a4c2991afe52f9975f8791412736762e59ee65a9924d2218ff34ff5cc53c84e6254'
            '3af927b8dde0b10ca45899016bce5e4f5b25ef285b2339a63346bfbfa99cc1a0e2f0728336c3ac7e32d4c05375f36fdfa7cf97cdfd26b42834cb3cb631d593b9'
            'ea8ed3537fb00596c16fa8b3464a2da54845ce9782e7bb40eb1157eb94de53892dda99bb4f22a829493cd59cfb47551f39de7641bf65a33678e97e5a4974de1a'
            'SKIP')

prepare() {
  # we don't use ninja from PyPI to build the package
  sed -i "/ninja/d" "${srcdir}/${_pkgname}-${pkgver}/pyproject.toml"
  patch -d "${srcdir}/${_pkgname}-${pkgver}" -p1 -i "${srcdir}/589.patch"
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
