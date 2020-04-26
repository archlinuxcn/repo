# Maintainer: goetzc
# Maintainer: James P. Harvey <jamespharvey20 at gmail dot com>

pkgname=python-spotipy
_pkgname=spotipy
pkgver=2.11.2
pkgrel=1
pkgdesc='Simple client for the Spotify Web API'
arch=(any)
url="https://github.com/plamere/spotipy"
license=(MIT)
makedepends=(python-setuptools git)
depends=(python-requests python-simplejson)
conflicts=(${pkgname}-git)
options=(!emptydirs)
source=("https://github.com/plamere/${_pkgname}/archive/${pkgver}.tar.gz")

pkgver() {
  cd ${_pkgname}-${pkgver}
  grep version setup.py | cut -d "=" -f 2 | grep -oP "(?<=\').*?(?=\')"
}

build() {
  cd ${_pkgname}-${pkgver}
  python setup.py build
}

package() {
  cd ${_pkgname}-${pkgver}
  python setup.py install --root="$pkgdir/" --skip-build --optimize=1
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha256sums=('9473201662ae72f0defcf95ff3ebfee57dfa2183955f9f90d7796b8ba7d81530')
