# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.30.2
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('31d4e3545b612fe21377b8dc48138d75fcd23b8c1b8423f15a69a717ee0ef647a4d62f6ff19ff8a1596b0049f459de414800d214b8fa7b53dc9f687dfed61678')
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
