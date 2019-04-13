# Contributor: Florian Klink <flokli at flokli dot de>
pkgname=python-pystache
_pkgname=pystache
pkgver=0.5.4
pkgrel=5
pkgdesc="The mustache template engine written in python"
arch=("any")
url="http://github.com/defunkt/pystache"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/defunkt/$_pkgname/archive/v$pkgver.tar.gz")
sha256sums=('163f5b8fb45f6be3a5074a53a47e79ef51ec015ee43f3ec34b16be279147c96f')

build() {
	cd "$_pkgname-$pkgver"
	python setup.py build
}

check() {
	# This package uses 2to3 to convert itself to Python 3 on the fly
	# So we need to jump through some hoops here
	rm -rf test_dir
	mkdir test_dir
	cd "$_pkgname-$pkgver"
	python setup.py install --root=../test_dir
	PYTHONPATH=../test_dir/usr/lib/python3.7/site-packages/ \
		../test_dir/usr/bin/pystache-test .
}

package() {
	cd "$_pkgname-$pkgver"
	python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
