# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.30.12
pkgrel=1
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('2756c086391eea66594d01ace2776e04a4c36ed706df0dcd9c13a93bd7c4ca97e90f69399b953de469cbb981731beb50853bc6b51b24212d1988b89876bf402d')
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
