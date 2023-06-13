# Maintainer: Lex Black <autumn-wind at web dot de>
# Contributor: Daniel Larsson <znixen@live.se>

pkgbase=patool
pkgname='patool'
pkgver=1.12
pkgrel=5
pkgdesc="portable command line archive file manager"
arch=('any')
url="https://wummel.github.io/patool/"
license=('GPL')
depends=('python')
makedepends=('python-setuptools')
optdepends=("tar: extracting TAR files"
    "unrar: extracting RAR files"
    "p7zip: extracting ZIP and 7z files")
#source=("https://pypi.python.org/packages/source/p/$pkgbase/$pkgbase-$pkgver.tar.gz")
source=("$pkgbase-$pkgver.tar.gz::https://github.com/wummel/patool/archive/upstream/${pkgver}.tar.gz")
sha256sums=('582fd4b87c263325958c1550400504799018c88bc3444f249bba304ae1747f1f')


build() {
  cd "${pkgbase}-upstream-${pkgver}"
  python setup.py build
}

package() {
  cd "${pkgbase}-upstream-${pkgver}"
  python setup.py install --root=$pkgdir --prefix=/usr --optimize=1 --skip-build
}
