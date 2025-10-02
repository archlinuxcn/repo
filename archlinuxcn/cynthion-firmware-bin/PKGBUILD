# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=cynthion-firmware-bin
_pypi_name=cynthion
pkgver=0.2.4
pkgrel=1
pkgdesc='Firmware for the Great Scott Gadgets Cynthion (pre-built from PyPI)'
arch=('any')
url='https://github.com/greatscottgadgets/cynthion'
license=('BSD-3-Clause')
optdepends=(
  'riscv64-linux-gnu-gdb: to debug the firmware over JTAG'
)
provides=("cynthion-firmware=${pkgver}")
conflicts=('cynthion-firmware')

source=(
  "${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pypi_name::1}/${_pypi_name}/${_pypi_name}-${pkgver}.tar.gz"
)

sha512sums=('555bb8c36a98a41a84649980da29f25a45bc49d87007291adbd4ecee414fc9618a88b8b7c31310a55f0304a6e3d2bedce0de1cf1bfa42e09075530f25e22cd2d')

package() {
  cd "${_pypi_name}-${pkgver}"

  echo >&2 'Packaging binaries'
  install -D -m 644 -t "${pkgdir}/usr/lib/${pkgname%-bin}" \
    assets/*.bin

  echo >&2 'Packaging bitstreams'
  cp -R --preserve=mode -t "${pkgdir}/usr/lib/${pkgname%-bin}" \
    assets/CynthionPlatform*

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE.txt
}
