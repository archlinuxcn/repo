# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=2.1.8
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-attrs' 'python-numpy' 'python-pillow' 'python-toml' 'python-yaml')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('2eb3386fb6510cd4e0172b2ad8bf8b1d136396595e7feaede1841db8cec33a92')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
