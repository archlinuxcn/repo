# Maintainer: Max Gautier <mg+archlinux@max.gautier.name>
pkgname=oauth2token
pkgver=0.0.3
pkgrel=1
pkgdesc="Simple cli utility to create and use oauth2 tokens"
arch=(any)
url="https://pypi.org/project/$pkgname/"
license=('GPL')
depends=(python-google-auth-oauthlib python-pyxdg)
makedepends=(python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$pkgname-$pkgver.tar.gz")
sha512sums=('9d3f708de37821892578b231c538302b39cd4c95053912bc01250e4a8d1d6acd1b204b1c53a8e956824ed0913439dba5d52a28d4dcd2cbd3d0db2a5455edb148')

build() {
	cd "$pkgname-$pkgver"
    python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
