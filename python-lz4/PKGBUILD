# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
pkgver=0.10.0
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools')
depends=('python3')
source=("https://pypi.python.org/packages/1b/69/6c106a77a804f08938487a9bf45a9771209f487c9dadea8ea819c1555e35/lz4-$pkgver.tar.gz")
md5sums=('46f2b225747703aa8b12e003604bdcef')

package() {
  cd $srcdir/lz4-$pkgver
  python3 setup.py install --root=$pkgdir || return 1
}
