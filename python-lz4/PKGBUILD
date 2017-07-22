# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
pkgver=0.10.1
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools')
depends=('python3')

source=("https://pypi.python.org/packages/f5/c6/ef2890b5e287735576e15c1389aa0b9032c9d78ed72385fbd1149af593cd/lz4-$pkgver.tar.gz")
md5sums=('1b8de6217e0785e92f457056c053e058')

package() {
  cd $srcdir/lz4-$pkgver
  python3 setup.py install --root=$pkgdir || return 1
}
