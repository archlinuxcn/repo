# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-types-setuptools
_name=${pkgname#python-}
pkgver=75.2.0.20241025
pkgrel=1
pkgdesc="Typing stubs for setuptools"
arch=('any')
url="https://github.com/python/typeshed"
license=('Apache-2.0')
depends=('python' 'python-types-docutils')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('2949913a518d5285ce00a3b7d88961c80a6e72ffb8f3da0a3f5650ea533bd45e')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
