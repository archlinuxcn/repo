# Maintainer: Max Gautier <ashelia1000 at gmail dot com>
pkgname=oauth2token
pkgver=0.0.2.post2
pkgrel=1
pkgdesc="Simple cli utility to create and use oauth2 tokens"
arch=(any)
url="https://pypi.org/project/$pkgname/"
install=
install=
license=('GPL')
depends=(python-google-auth-oauthlib python-pyxdg)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha512sums=('12a59f911e66dde8fd62ab014349afbd09785273fbf0b7b004857a114d1187d2ad9bd3740989a74de58ac26145ece60ac07fece55d73a9564a16a0f6780cc65f')

build() {
	cd "$pkgname-$pkgver"
    python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
