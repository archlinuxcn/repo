# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.30.4
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('81739ee8d3eb7b9b33bce2bd2f1d04ce94c09d692f91da3341fbf4bd986f9e8f91e845af32093b1d0eeaf925150bbdd8f8a108dda64e829ffc823f04ff95af40')
depends=('beancount' 'beanquery' 'beangulp' 'python-click' 'python-markdown2' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-ply' 'python-simplejson' 'python-watchfiles')
makedepends=("python-build" "python-installer" "python-wheel" "python-setuptools-scm" "npm")

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
