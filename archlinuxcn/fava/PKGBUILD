# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.23.1
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/py3/f/fava/fava-${pkgver}-py3-none-any.whl")
noextract=("fava-${pkgver}-py3-none-any.whl")
sha256sums=('0fe8c64a6842478ace78fbfd56379c620723bc7b0e9a98aabe09515b0249fc4b')
depends=('beancount' 'python-setuptools' 'python-click' 'python-markdown2' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-simplejson')
makedepends=('python-pip')

package () {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps fava-${pkgver}-py3-none-any.whl
  python -O -m compileall "${pkgdir}/usr/lib/python3.10/site-packages/${pkgname}/"
}
