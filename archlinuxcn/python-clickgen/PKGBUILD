# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=2.1.7
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-attrs' 'python-numpy' 'python-pillow' 'python-toml' 'python-yaml')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('f335d1ab2267c047aa2fb608b64419e70c3b81e1a6715c32b0170bc30cd52699')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
