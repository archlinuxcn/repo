# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>

pkgname=python-sphinx_rtd_dark_mode
pkgver=1.3.0
pkgrel=1
pkgdesc='Adds a toggleable dark mode to the Read the Docs theme.'
arch=('any')
url='https://github.com/MrDogeBro/sphinx_rtd_dark_mode'
license=('MIT')
depends=('python-sphinx_rtd_theme')
makedepends=('python-setuptools-scm' 'python-build' 'python-installer' 'python-wheel')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
b2sums=('2e7dffcd02dfc4103f7069a65b569a3d2f2f7ec5b51384afe8c04753124a096fd713f04db9e4afbd20cfdc6a187df02b10ff2b802f51cd9d54c305c4aad507b7')
_srcdir="sphinx_rtd_dark_mode-${pkgver}"

build() {
  cd "$_srcdir"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_srcdir"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname LICENSE
}
