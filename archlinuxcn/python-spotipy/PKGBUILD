# Maintainer: goetzc
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>
# Maintainer: Vyacheslav Konovalov <vyachkonovalov@protonmail.com>

_pkgname=spotipy
pkgname=python-spotipy
pkgver=2.16.1
pkgrel=1
pkgdesc='A light weight Python library for the Spotify Web API'
arch=('any')
url='https://github.com/plamere/spotipy'
license=('MIT')
depends=('python-requests' 'python-six')
makedepends=('python-setuptools')
conflicts=("$pkgname-git")
source=("$pkgname-$pkgver.tar.gz::https://github.com/plamere/spotipy/archive/$pkgver.tar.gz")

build() {
  cd spotipy-$pkgver
  python setup.py build
}

package() {
  cd spotipy-$pkgver
  python setup.py install --root="$pkgdir" --skip-build --optimize=1
  install -Dm644 LICENSE.md -t "$pkgdir/usr/share/licenses/$pkgname"
}

sha256sums=('1b8c9251859b26a93e7de6f17753ed76d25212e668207f060d844d828df64ea6')
