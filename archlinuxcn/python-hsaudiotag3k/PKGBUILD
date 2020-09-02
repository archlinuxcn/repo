# vim:set ts=2 sw=2 et:
# Maintainer: Martin Rys <https://rys.pw/#contact_me>
# Previous maintainer: Bijaya Dangol <dangoldbj23@gmail.com>

pkgname=python-hsaudiotag3k
_reponame=hsaudiotag3k
pkgver=1.1.3.post1
pkgrel=1
pkgdesc="Read metadata (tags) of mp3, mp4, wma, ogg, flac and aiff files (python3 version)"
url="https://pypi.python.org/pypi/hsaudiotag3k"
arch=(any)
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://pypi.python.org/packages/source/h/${_reponame}/${_reponame}-$pkgver.tar.gz")
sha256sums=('ef60e9210d4727e82f0095a686cb07b676d055918f0c59c5bfa8598da03e59d1')

build() {
  cd "$srcdir/${_reponame}-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/${_reponame}-$pkgver"
  python setup.py install --root="$pkgdir"
}
