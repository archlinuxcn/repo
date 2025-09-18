# Maintainer: Markus Koch <markus@notsyncing.net>

pkgname=python-fx2-git
pkgver=v0.13.r2.g0134160
pkgrel=1
pkgdesc="Allow interacting with Cypress EZ-USB FX2 series microcontrollers"
arch=('any')
url='https://github.com/whitequark/libfx2'
license=('0BSD')
depends=('python' 'python-libusb1')
makedepends=('git' 'python-setuptools')
source=("git+https://github.com/whitequark/libfx2.git")
sha256sums=('SKIP')
provides=('python-fx2')

pkgver() {
	cd "$srcdir/libfx2"
	git describe --tags --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "$srcdir/libfx2/software"
	python setup.py build
}

package() {
	cd "$srcdir/libfx2/software"
	python setup.py install --optimize=1 --root="${pkgdir}/"
}
