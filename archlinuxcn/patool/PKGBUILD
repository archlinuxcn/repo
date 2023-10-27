# Maintainer: Lex Black <autumn-wind at web dot de>
# Contributor: Daniel Larsson <znixen@live.se>

pkgbase=patool
pkgname='patool'
pkgver=1.14.1
pkgrel=2
pkgdesc="portable command line archive file manager"
arch=('any')
url="https://wummel.github.io/patool/"
license=('GPL')
depends=('python')
makedepends=(python-build python-installer python-wheel python-setuptools)
optdepends=("tar: extracting TAR files"
    "unrar: extracting RAR files"
    "p7zip: extracting ZIP and 7z files"
    "zstd: extracting ZSTANDARD files")
#source=("https://pypi.python.org/packages/source/p/$pkgbase/$pkgbase-$pkgver.tar.gz")
source=("$pkgbase-$pkgver.tar.gz::https://github.com/wummel/patool/archive/upstream/${pkgver}.tar.gz")
sha256sums=('51b2abdd4ccd9eb93884e61fc401295d8990b30c8c98d70c24bb835a21ec27e0')


build() {
  cd "${pkgbase}-upstream-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgbase}-upstream-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
