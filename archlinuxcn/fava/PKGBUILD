# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.27.3
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/py3/f/fava/fava-${pkgver}-py3-none-any.whl")
noextract=("fava-${pkgver}-py3-none-any.whl")
sha256sums=('7b12527e2f469285e797f6015b0933fb160da50e470fa2f57379eb3e621a0466')
depends=('beancount' 'python-setuptools' 'python-click' 'python-markdown2' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-simplejson')
makedepends=('python-pip')

package () {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps --no-warn-script-location fava-${pkgver}-py3-none-any.whl
  python -O -m compileall "${pkgdir}/usr/lib/python3.*/site-packages/${pkgname}/"
}
