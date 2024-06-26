# Maintainer: Andrew O'Neill <andrew at haunted dot sh>

pkgname=python-oci
_pyname=oci-python-sdk
pkgver=2.128.2
pkgrel=1
pkgdesc='Python SDK for Oracle Cloud Infrastructure'
arch=('x86_64')
url="https://github.com/oracle/${_pyname}"
license=('Apache-2.0 OR UPL-1.0')
depends=('python' 'python-dateutil' 'python-certifi' 'python-circuitbreaker' 'python-cryptography' 'python-pyopenssl' 'python-pytz')
makedepends=('python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('836cb41416e4a57feaee89623aa0650433f3bb88d75816562c60b57fcc749996')

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
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
