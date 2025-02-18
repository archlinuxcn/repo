# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-types-setuptools
_name=types_setuptools
pkgver=75.8.0.20250210
pkgrel=1
pkgdesc="Typing stubs for setuptools"
arch=('any')
url="https://github.com/python/typeshed"
license=('Apache-2.0')
depends=(
  'python'
  'python-types-docutils'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('c1547361b2441f07c94e25dce8a068e18c611593ad4b6fdd727b1a8f5d1fda33')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
