# Maintainer: Andrew O'Neill <andrew at haunted dot sh>

pkgname=python-oci
_pyname=oci-python-sdk
pkgver=2.187.0
pkgrel=1
pkgdesc='Python SDK for Oracle Cloud Infrastructure'
arch=('any')
options=('!strip')
url="https://github.com/oracle/${_pyname}"
license=('Apache-2.0 OR UPL-1.0')
depends=('python' 'python-aiohttp' 'python-dateutil' 'python-certifi' 'python-circuitbreaker' 'python-crc32c' 'python-cryptography' 'python-pyjwt' 'python-pyopenssl' 'python-pytz' 'python-urllib3')
makedepends=('python-setuptools' 'python-wheel')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('4e8ecd38cb1e89b2eef5738e953f6a8752cc9541052514e14625c48bc839b224')

prepare() {
  cd "${_pyname}-${pkgver}"

  sed -i -r 's/(==|>|<).*"/"/g' setup.py
  sed -i '/configparser/d' setup.py
}

build() {
  cd "${_pyname}-${pkgver}"

  python setup.py build
}

package() {
  cd "${_pyname}-$pkgver"

  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE.txt "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE
}
