# Maintainer: Y7n05h <Y7n05h(aT)protonmail--d0t--com>
pkgname=python-timeslot
_name=${pkgname#python-}
pkgver=0.1.2
pkgrel=1
pkgdesc="Time slots/intervals with an arbitrary start and stop"
arch=('any')
url="https://github.com/ErikBjare/timeslot"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
provides=($pkgname)
conflicts=()
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('a2ac998657e3f3b9ca928757b4906add2c05390c5fc14ed792bb9028d08547b1')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build

}
