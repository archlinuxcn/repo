# Maintainer: Christian Rebischke <chris.rebischke[at]archlinux[dot]org>

pkgbase=python-requests-cache
_pyname=requests-cache
pkgname=('python-requests-cache' 'python2-requests-cache')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools'
             'python-requests' 'python2-requests')
pkgver=0.4.13
pkgrel=1
pkgdesc="Persistent cache for requests library"
arch=('any')
url="https://github.com/reclosedev/requests-cache"
license=('BSD')
source=("${_pyname}-${pkgver}.tar.gz::https://github.com/reclosedev/${_pyname}/archive/v${pkgver}.tar.gz")
sha512sums=('54d814c9c4da1b1fa6f4ec124faee7e74e7ca52bc90ae7c948f19e9cb7657fe2b41f5de6c5fafe259526312d82dc5efd81ad01a741a66baf12ea2a358334f912')

package_python-requests-cache() {
  depends=('python')
  cd "${srcdir}/${_pyname}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 README.rst "${pkgdir}/usr/share/doc/${pkgname}/README"

}

package_python2-requests-cache() {
  depends=('python2')
  cd "${srcdir}/${_pyname}-${pkgver}"
  python2 setup.py install -O1 --root="${pkgdir}"
  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 README.rst "${pkgdir}/usr/share/doc/${pkgname}/README"

}

# vim:set et sw=2 ts=2 tw=79:
