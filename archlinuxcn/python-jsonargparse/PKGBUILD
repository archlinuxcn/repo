# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=jsonargparse
pkgname=python-jsonargparse
pkgver=4.10.1
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
sha512sums=('85d647ec071abcb2ab6d45cc253211f69ee715e89c0c6a8f264dd138ce4cdb75efa9d889a1428e8d652a949cf71a7d9e9d8aa455d497acacb37a4e9b6fd4abd2')

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
