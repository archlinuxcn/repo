# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Payson Wallach <payson@paysonwallach.com>

pkgname=python-persist-queue
pkgver=0.7.0
pkgrel=1
pkgdesc='Thread-safe disk-based persistent queue'
arch=(any)
url="https://github.com/peter-wangxu/persist-queue"
license=('BSD')
depends=('python')
optdepends=('python-msgpack>=0.5.6')
makedepends=('python-setuptools')
checkdepends=('python-nose2' 'python-msgpack>=0.5.6' 'python-mock>=2.0.0' 'python-eventlet>=0.19.0')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('720d47b022f4f4811ab67f9db665cc1fe1e83455cfd1fe26b13478f04a7c24f6')

prepare() {
	cd "persist-queue-$pkgver"
	sed -i "/packages=find/c\packages=find_packages(exclude=('*tests*',))," setup.py
}

build() {
	cd "persist-queue-$pkgver"
	python setup.py build
}

check() {
	cd "persist-queue-$pkgver"
	nose2
}

package() {
	cd "persist-queue-$pkgver"
	PYTHONHASHSEED=0 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
	install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
	install -Dm 644 README.rst -t "$pkgdir/usr/share/doc/$pkgname/"
}
