# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=jsonargparse
pkgname=python-jsonargparse
pkgver=4.6.0.dev1
pkgrel=1
pkgdesc='Parsing of command line options, yaml/jsonnet config files and/or environment variables based on argparse'
arch=('any')
url='https://github.com/omni-us/jsonargparse'
license=('MIT')
depends=(
  python-yaml
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/omni-us/jsonargparse/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b77871f9a3c6a315a4e226c64ef52454ef5d7e8754251d5f14966f737c22bca5cfec9db99f17b7603c2bf4a32ec7f48783a27623a3d8deffc63d11626f910b65')

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
  install -Dm644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/jsonargparse_tests"
}
# vim:set ts=2 sw=2 et:
