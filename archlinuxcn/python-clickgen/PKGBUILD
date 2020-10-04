# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=1.1.6
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-pillow' 'libx11' 'libxcursor' 'libpng')
makedepends=('python-setuptools' 'python-pip')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('e5197dd6b8e9bedb0ee76b3b46c2db54f0edbbd260fda17ab1bccb57eff0dfb5')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build

	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
