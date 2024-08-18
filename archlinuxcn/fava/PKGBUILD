# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.28
pkgrel=2
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/py3/f/fava/fava-${pkgver}-py3-none-any.whl")
noextract=("fava-${pkgver}-py3-none-any.whl")
sha256sums=('44f7f8b3d11e70592a3412ced564ca4b6750c910e43f769b6582febb51eee7db')
depends=('beancount' 'python-setuptools' 'python-click' 'python-markdown2' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-simplejson' 'python-watchfiles')
makedepends=('python-pip')

package () {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps --no-warn-script-location fava-${pkgver}-py3-none-any.whl
  python -O -m compileall "${pkgdir}/usr/lib/python3.*/site-packages/${pkgname}/"
}
