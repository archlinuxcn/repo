# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=2.1.1
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-attrs' 'python-pillow' 'python-toml')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
#checkdepends=('python-pytest-cov')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('43ca89b99989664654ec99fe72cb18a43f679b2b152720312156e26704864d83')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

#check() {
#  cd "$_name-$pkgver"
#  pytest --cov=clickgen --cov-report=html
#}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
