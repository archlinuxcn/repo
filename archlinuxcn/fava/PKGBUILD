# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=fava
pkgdesc='Web interface for beancount'
pkgver=1.31
pkgrel=2
arch=('any')
url='https://github.com/beancount/fava'
license=('MIT')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
noextract=("fava-${pkgver}-py3-none-any.whl")
b2sums=('ef1e970e2a83018b269c6a01843c7a44417ec7f3e59ddec59b7fee440083c31a6c6891fc056f2d3aaae1152d718b03702203c97bc64fb721cfa550fd7d8fbee3')
depends=('beancount' 'beanquery' 'beangulp' 'python-click' 'python-markdown-it-py' 'python-flask' 'python-flask-babel' 'python-cheroot' 'python-watchfiles' 'python-msgspec')
makedepends=("python-build" "python-installer" "python-hatchling" "python-hatch-vcs" "npm")

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
