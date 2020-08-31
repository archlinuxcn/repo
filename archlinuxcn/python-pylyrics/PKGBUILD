# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=python-pylyrics
_name=PyLyrics
pkgver=1.1.0
pkgrel=1
pkgdesc="A Pythonic Implementation of lyrics.wikia.com for getting lyrics of songs"
arch=('any')
url="https://github.com/geekpradd/PyLyrics"
license=('GPL')
depends=('python-beautifulsoup4' 'python-requests')
makedepends=('python-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.zip")
sha256sums=('c5f36e8ef0ed3b487a9242ce34c19f9684e418a5bbffd5d367dc1d1604b4cd0b')

build() {
	cd "$_name-$pkgver"
	python setup.py build
}

package() {
	cd "$_name-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
