# Maintainer:
pkgname=python-colorful
_name=${pkgname#python-}
pkgver=0.5.4
pkgrel=2
pkgdesc="Terminal string styling done right, in Python"
arch=('any')
url="https://github.com/timofurrer/colorful"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('86848ad4e2eda60cd2519d8698945d22f6f6551e23e95f3f14dfbb60997807ea')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
