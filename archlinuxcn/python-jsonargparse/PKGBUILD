# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=jsonargparse
pkgname=python-jsonargparse
pkgver=4.15.1
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
sha512sums=('899d7d0ec7cf1eba24bc1338cddbb47f78b63fd4686333ee86300096d8477d4fb90c48ad5e3f5d421b5daa59d495c55c9fb80d1e3bf59c1719b3441fc753c91d')

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
