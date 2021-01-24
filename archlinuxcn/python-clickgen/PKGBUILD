# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=1.1.8
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=('python-pillow' 'libx11' 'libxcursor' 'libpng')
makedepends=('python-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('ec853050a433dac806cbf7b428427a9ae6fd2536012bc3e5e8e194789396f9b2')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	export PYTHONHASHSEED=0
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build

	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
