# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-types-setuptools
_name=types_setuptools
pkgver=80.0.0.20250429
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
sha256sums=('a4de44f1110f531e7f9453d72999437a1caa6052609e2c7c859dd6613ab0d593')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
