# Maintainer: Chen Mulong <chenmulong@gmail.com>

pkgname=python-pygresql
pkgver=5.2.2
pkgrel=1
pkgdesc="PyGreSQL is an open-source Python module that interfaces to a PostgreSQL database."
arch=('x86_64')
url="https://pygresql.org/"
license=('PostgreSQL')
depends=()
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/79/e5/05f941e588d48d0b742850b74e991b29502f1e46194bbf5449e5632388ee/PyGreSQL-${pkgver}.tar.gz")
sha256sums=('114f60dc486bf4967aad14dc3adde5e4f60a35eea1eb8f7b8f0ae15c21b6f4a5')

build() {
  cd PyGreSQL-$pkgver
  python setup.py build
}

package() {
  cd PyGreSQL-$pkgver
  python setup.py install --prefix=/usr --root="$pkgdir"
}
