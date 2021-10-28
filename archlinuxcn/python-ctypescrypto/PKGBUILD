# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='ctypescrypto'
pkgbase='python-ctypescrypto'
pkgname=('python-ctypescrypto' 'python2-ctypescrypto')
pkgver='0.5'
pkgrel='1'
pkgdesc='Python interface to some openssl function based on ctypes module'
arch=('any')
url="https://github.com/vbwagner/${_name}"
makedepends=('python' 'python-setuptools'
	     'python2' 'python2-setuptools')
license=('MIT')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('7258fad7d025ed3dc4bbe1dc24e6cf1842481216837615e9892596e06c942602')

package_python-ctypescrypto() {
  depends=('python')

  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
}

package_python2-ctypescrypto() {
  depends=('python2')

  cd "${srcdir}/${_name}-${pkgver}"
  python2 setup.py install -O1 --root="${pkgdir}"
}
