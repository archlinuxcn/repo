# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.10
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('GPL')
source=("https://files.pythonhosted.org/packages/py3/f/fava/fava-${pkgver}-py3-none-any.whl")
noextract=("fava-${pkgver}-py3-none-any.whl")
sha256sums=('e8345268404a5cf3d0817aecd3ba830b3feec3911bcafd4a175a5d5bedde77de')
depends=('beancount' 'python-pip' 'python-click' 'python-markdown2' 'python-flask' 'python-flask-babel' 'python-cheroot')

package () {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps fava-${pkgver}-py3-none-any.whl
  python -O -m compileall "${pkgdir}/usr/lib/python3.7/site-packages/${pkgname}/"
}
