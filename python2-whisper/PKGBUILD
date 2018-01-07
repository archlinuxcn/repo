Maintainer='Gilles Hamel <hamelg@laposte.net>'
pkgname=python2-whisper
pkgver=1.1.1
pkgrel=1
pkgdesc='Fixed-size database that provides fast, reliable storage of numeric data over time.'
arch=('any')
url='https://github.com/graphite-project/whisper'
license=('Apache')
depends=('python2')
makedepends=('python2-setuptools')
options=(!emptydirs)
source=($pkgname-$pkgver.tar.gz::"https://github.com/graphite-project/whisper/archive/$pkgver.tar.gz")
md5sums=('b53cc28abd22e4d75daa95169bf3a4e5')

package() {
  cd "$srcdir/whisper-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
