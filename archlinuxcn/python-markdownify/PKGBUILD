# Maintainer:
# Contributor: Bjoern Franke <bjo+aur@schafweide.org>

_module="markdownify"
_pkgname="python-$_module"
pkgname="$_pkgname"
pkgver=0.14.1
pkgrel=1
pkgdesc="Convert HTML to Markdown"
url="https://github.com/matthewwithanm/python-markdownify"
license=('MIT')
arch=('any')

depends=(
  'python'
  'python-beautifulsoup4'
  'python-six'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools-scm'
  'python-wheel'
)

_pkgsrc="$_module-$pkgver"
_pkgext="tar.gz"
source=(
  "$_pkgsrc.$_pkgext"::"https://pypi.io/packages/source/${_module::1}/$_module/$_module-$pkgver.$_pkgext"
)
sha256sums=(
  'a62a7a216947ed0b8dafb95b99b2ef4a0edd1e18d5653c656f68f03db2bfb2f1'
)

build() {
  cd "$_pkgsrc"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_pkgsrc"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
