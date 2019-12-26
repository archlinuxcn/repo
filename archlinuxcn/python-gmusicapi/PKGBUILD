# Maintainer: robertfoster
# Contributor: Robert Booster > booster.devel@gmail.com

pkgbase=python-gmusicapi
pkgname=python-gmusicapi
pkgver="12.1.1"
pkgrel=2
pkgdesc="An unofficial client library for Google Music"
arch=('any')
url="https://github.com/simon-weber/gmusicapi"
license=('BSD')
makedepends=('python-setuptools')
source=("https://github.com/simon-weber/gmusicapi/archive/$pkgver.tar.gz")
conflicts=("${pkgname}-git")
provides=("${pkgname}")
depends=('python-validictory' 'python-decorator' 'python-requests' 'python-dateutil'
         'python-proboscis' 'python-protobuf' 'python-oauth2client' 'python-mock'
         'python-appdirs' 'python-gpsoauth' 'python-mechanicalsoup' 'python-six' 'python-future' 'python-mutagen')

package() {
	cd "${pkgname##python-}-$pkgver"
	python setup.py install --root="$pkgdir" --optimize=1
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

md5sums=('3ec1bd2da0520e5531a4ac6ee7331571')
