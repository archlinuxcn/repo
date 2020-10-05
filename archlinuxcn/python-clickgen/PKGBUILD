# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=1.1.7
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-pillow' 'libx11' 'libxcursor' 'libpng')
makedepends=('python-setuptools' 'python-pip')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('5aaaedd34d7115976db9b82e1d57492d7aceedd5c00a43155d86cbb11073444e')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build

	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
