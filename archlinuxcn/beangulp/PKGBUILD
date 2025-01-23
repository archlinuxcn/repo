# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=beangulp
pkgdesc='Importers framework for Beancount'
pkgver=0.2.0
pkgrel=1
arch=("any")
url="https://github.com/beancount/beangulp"
license=('GPL')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
b2sums=('4dadb2a9d289cc282c353dba413a77cdd5f99cb8e8d869238e8a78b22e59d031c8db890f440fc8d06092a7aae0441d3564bf5427084a97c6a9c550ebe4d580c3')
depends=("python" "beancount>=3" "python-beautifulsoup4" "python-chardet" "python-click" "python-lxml" "python-magic")
makedepends=("python-build" "python-installer" "python-wheel" "python-setuptools")

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
