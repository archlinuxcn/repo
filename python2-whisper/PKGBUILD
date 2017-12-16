Maintainer='Gilles Hamel <hamelg@laposte.net>'
pkgname=python2-whisper
pkgver=1.0.2
pkgrel=1
pkgdesc='Fixed-size database that provides fast, reliable storage of numeric data over time.'
arch=('any')
url='https://github.com/graphite-project/whisper'
license=('Apache')
depends=('python2')
makedepends=('python2-setuptools')
options=(!emptydirs)
source=("https://github.com/graphite-project/whisper/archive/$pkgver.tar.gz")
md5sums=('466d2a7dde27554b4fdaf6e7cd570c57')

package() {
  cd "$srcdir/whisper-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
