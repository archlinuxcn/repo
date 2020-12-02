# Maintainer: robertfoster
# Contributor: Robert Booster > booster.devel@gmail.com

pkgbase=python-gmusicapi
pkgname=python-gmusicapi
pkgver="13.0.0"
pkgrel=2
pkgdesc="An unofficial client library for Google Music"
arch=('any')
url="https://github.com/simon-weber/gmusicapi"
license=('BSD')
makedepends=('python-setuptools')
source=("https://github.com/simon-weber/gmusicapi/archive/$pkgver.tar.gz")
conflicts=("${pkgname}-git")
provides=("${pkgname}")
depends=('python-appdirs' 'python-dateutil' 'python-decorator' 'python-gpsoauth'
    'python-mechanicalsoup' 'python-mock' 'python-mutagen' 'python-oauth2client'
'python-proboscis' 'python-protobuf' 'python-requests' 'python-validictory')

package() {
    cd "${pkgname##python-}-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

md5sums=('ce06c4cc1aa34946814c57b75f4132ae')
