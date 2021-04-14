# Maintainer: goetzc
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Maintainer: Vyacheslav Konovalov <crabvk@protonmail.com>

_pkgname=spotipy
pkgname=python-spotipy
pkgver=2.18.0
pkgrel=1
pkgdesc='A light weight Python library for the Spotify Web API'
arch=('any')
url='https://github.com/plamere/spotipy'
license=('MIT')
depends=('python-requests' 'python-six')
makedepends=('python-setuptools')
conflicts=("$pkgname-git")
source=("$pkgname-$pkgver.tar.gz::https://github.com/plamere/spotipy/archive/$pkgver.tar.gz")
sha512sums=('3be69c5be4a491d01612f39292c7833e3e04fc25b3ffca72af492d31aa56289c73cc19d04324240a5f3c1eb0db8ab9b07ed42777fc6bb89c8898f84c76fd873e')

build() {
  cd spotipy-$pkgver
  python setup.py build
}

package() {
  cd spotipy-$pkgver
  python setup.py install --root="$pkgdir" --skip-build --optimize=1
  install -Dm644 LICENSE.md -t "$pkgdir/usr/share/licenses/$pkgname"
}
