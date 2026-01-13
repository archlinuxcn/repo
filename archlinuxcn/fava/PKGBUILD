# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.30.10
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('d662632f16cf4299aea63b9947ea3795f6e98cf0bceb34cd009ebfe51682d2d00376d8aa8d94931ee641618e4ab572a4a116a94d79cd872814df8f305da42929')
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
