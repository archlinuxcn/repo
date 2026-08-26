# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.30.16
pkgrel=2
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('183e382957f1d640392362252ecf4452850cf69ccf2012b580592e44418d9d69bcbc7313dec4e3e344bf53aeed41255922131567d9c3588268ba17520eebe04e')
depends=('beancount' 'beanquery' 'beangulp' 'python-click' 'python-markdown-it-py' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-ply' 'python-simplejson' 'python-watchfiles')
makedepends=("python-build" "python-installer" "python-hatchling" "python-hatch-vcs" "npm")

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
