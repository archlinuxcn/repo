# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=1.2.0
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('x86_64')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-pillow' 'libx11' 'libxcursor' 'libpng')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
provides=('xcursorgen.so')
source=("$_name-$pkgver.tar.gz::https://github.com/ful1e5/clickgen/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('26d5fccced30a635e9a113bac2c71f7fcea95cb73cd904ae1405c16ef172b88f')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation

  make -C src/xcursorgen
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -Dm644 src/xcursorgen/xcursorgen.so -t "${pkgdir}${site_packages}/$_name/"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "$site_packages/$_name-$pkgver.dist-info/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/"
}
