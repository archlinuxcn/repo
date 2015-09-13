# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=python2-pika
pkgver=0.10.0
pkgrel=1
_libname=${pkgname/python2-/}
pkgdesc="Pure-Python implementation of the AMQP 0-9-1"
arch=(any)
url="http://pika.readthedocs.org/"
license=('GPL')
depends=(python2)
makedepends=(python2-setuptools)
source=(http://pypi.python.org/packages/source/${_libname:0:1}/$_libname/$_libname-$pkgver.tar.gz)

build() {
  cd "$srcdir/$_libname-$pkgver"
  python2 setup.py build
}

package() {
	cd "$srcdir/$_libname-$pkgver"
	python2 setup.py install --skip-build -O1 --root="$pkgdir"
}

sha256sums=('7277b4d12a99efa4058782614d84138983f9f89d690bdfcea66290d810806459')
