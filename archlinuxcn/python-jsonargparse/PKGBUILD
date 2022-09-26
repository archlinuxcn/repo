# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=jsonargparse
pkgname=python-jsonargparse
pkgver=4.14.1
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
sha512sums=('547a5824a0e66bd4f12a5bc271ad780e7baa7f311ce6a667e4cde9444c3f0fc3075139f0ccf84abe15388c35e097f2dcb76238f9a671d8cee6bbeece696c4178')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -rf "${pkgdir}${site_packages}/jsonargparse_tests"
}
# vim:set ts=2 sw=2 et:
