# Maintainer: Evangelos Foutras <foutrelis@archlinux.org>
# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>

_name=recommonmark
pkgname=python-recommonmark
pkgver=0.7.1
pkgrel=9
pkgdesc='Markdown parser for docutils'
arch=('any')
url="https://recommonmark.readthedocs.io/"
license=('MIT')
depends=('python' 'python-commonmark' 'python-docutils' 'python-sphinx')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-pytest')
source=(https://files.pythonhosted.org/packages/source/r/$_name/$_name-$pkgver.tar.gz
        fix-many-warnings.patch
        autostructify-tab_width-fallback.patch)
sha256sums=('bdb4db649f2222dcd8d2d844f0006b958d627f732415d399791ee436a3686d67'
            '1a87d217d685b38e87fe67a6726b31f3e25333280da8e88dc7b52e93b7881f67'
            '0672b55c9bd49d24cfe86cd29fa93d1ebde3f757df606e7aea74ba6e58deff26')

prepare() {
  cd $_name-$pkgver
  patch -Np1 -i ../autostructify-tab_width-fallback.patch
  patch -Np1 -i ../fix-many-warnings.patch
}

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  make -C docs text man
}

check() {
  cd $_name-$pkgver
  PYTHONDONTWRITEBYTECODE=1 pytest --deselect tests/test_sphinx.py
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" license.md
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" \
    README.md CHANGELOG.md docs/_build/text/*.txt
  install -Dm644 -t "$pkgdir/usr/share/man/man1" docs/_build/man/$_name.1
}

# vim:set ts=2 sw=2 et:
