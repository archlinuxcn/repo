# Maintainer: goetzc
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>

pkgname=python-spotipy
_pkgname=spotipy
pkgver=2.4.4
pkgrel=2
pkgdesc='Simple client for the Spotify Web API'
arch=(any)
url="https://github.com/plamere/spotipy"
license=(MIT)
makedepends=(python-setuptools git)
depends=('python-requests' python-simplejson)
conflicts=(${pkgname}-git)
options=(!emptydirs)
_commit=bf219eb264a414f952106fbdf987c2f26206a5cd
source=("git+https://github.com/plamere/${_pkgname}/#commit=$_commit")
md5sums=('SKIP')

pkgver() {
  cd ${_pkgname}
  grep version setup.py |cut -f 2 -d "=" |grep -oP "(?<=\').*?(?=\')"
}

build() {
  cd ${_pkgname}
  python setup.py build
}

package() {
  cd ${_pkgname}
  python setup.py install --root="$pkgdir/" --skip-build --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
