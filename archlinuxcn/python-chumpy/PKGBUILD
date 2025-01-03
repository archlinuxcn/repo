# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=chumpy
pkgname=python-chumpy
pkgver=0.71
pkgrel=2
pkgdesc='Autodifferentiation tool for Python'
arch=('any')
url='https://github.com/mattloper/chumpy'
license=('MIT')
depends=(
  python-numpy
  python-scipy
  python-six
)
makedepends=(
  git
  python-build
  python-installer
  python-wheel
  python-setuptools
  python-pip
)
# there is no git tags available on github
# we use the latest commit as it fix many bugs
_commit=51d5afd92a8ded3637553be8cef41f328a1c863a
source=("${_pkgname}-${pkgver}::git+https://github.com/mattloper/chumpy.git#commit=${_commit}"
        "0001-fix-inspect.getargspec-issue.patch"
        "LICENSE::https://github.com/mattloper/chumpy/raw/master/LICENSE.txt"
)
sha512sums=('70dff9df49bd9a914de36df2c11011b2a120ee71bfb7e6937cbd1c8475c83980c7bba67cad1931e3b9ab641cba794cb2e5f0351428d647620f8ded90eeb4999e'
            'e4b802cb744fb0a5d9e5b01b709373f095f7e79fb02531f02eefc180585b9995fd22f294b94b43918962c0d44ab5ffee739b38b4750cbe0f427d0c8a05e868df'
            'dffa3b1e3f03ff837da0071f9cdd8b47198c6dd87e4a90bdf601711dde59be65798fb2ae0ed1aa3efe2660c9f76dff18c17f0b1cc0eb77f6ee871efc3d559c24')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-fix-inspect.getargspec-issue.patch"
}

build() {
  cd "${_pkgname}-${pkgver}"
  # python setup.py build
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  # python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
