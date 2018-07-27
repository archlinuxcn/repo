# Maintainer: Leo Schwarz (evotopid) <mail@leoschwarz.com>
pkgname=python-fakeredis
pkgver=0.8.2
pkgrel=1
pkgdesc="Fake implementation of redis API (redis-py) for testing purposes"
arch=('any')
url="https://github.com/jamesls/fakeredis"
license=('BSD')
depends=('python' 'python-redis')
checkdepends=('python-nose')
options=(!emptydirs)
source=("https://github.com/jamesls/fakeredis/archive/$pkgver.tar.gz")
md5sums=('2ad504d9f52cd026c3a61167bfbb882e')

package() {
  cd "$srcdir/fakeredis-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

check() {
  cd "$srcdir/fakeredis-$pkgver"
  python setup.py test
}

# vim:set ts=2 sw=2 et:
