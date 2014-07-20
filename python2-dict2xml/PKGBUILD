# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-dict2xml
_pypiname=dict2xml
pkgver=1.3
pkgrel=1
pkgdesc="Super Simple utility to convert a python dictionary into an xml string"
arch=('any')
url="https://github.com/delfick/python-dict2xml"
license=('GPL2')
depends=('python2')
source=("https://pypi.python.org/packages/source/d/dict2xml/${_pypiname}-${pkgver}.tar.gz")
sha512sums=('25cd5c8e0210b28e7428b36dac59b11c481c35b6e9946a6f9e4341ae49d013f6e0f119501b8ac6d427e07ea964ff2bfc862d1c0a8c69f0303665d4f84634f24a')

package() {
  cd "${srcdir}/${_pypiname}-${pkgver}"
  python2 setup.py install --root "${pkgdir}"
}

