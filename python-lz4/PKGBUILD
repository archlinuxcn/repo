# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
pkgver=0.9.2
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools')
depends=('python3')
source=("https://pypi.python.org/packages/47/19/eff906f3f37680a73ad9524eeee1a4f59f728b3a13a4bcd92251961d006b/lz4-$pkgver.tar.gz")
md5sums=('b11f78c4bfd2afb15b1094438735c689')

package() {
  cd $srcdir/lz4-$pkgver
  python3 setup.py install --root=$pkgdir || return 1
}
