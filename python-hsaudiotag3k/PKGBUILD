# vim:set ts=2 sw=2 et:
# Maintainer: Bijaya Dangol <dangoldbj23@gmail.com>

pkgname=python-hsaudiotag3k
_reponame=hsaudiotag3k
pkgver=1.1.3
pkgrel=2
pkgdesc="Read metadata (tags) of mp3, mp4, wma, ogg, flac and aiff files (python3 version)"
url="https://pypi.python.org/pypi/hsaudiotag3k"
arch=(any)
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://pypi.python.org/packages/source/h/${_reponame}/${_reponame}-$pkgver.tar.gz")
md5sums=('77fc873857303e889851605e9836669b')

build() {
  cd "$srcdir/${_reponame}-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/${_reponame}-$pkgver"
  python3 setup.py install --root="$pkgdir"
}
