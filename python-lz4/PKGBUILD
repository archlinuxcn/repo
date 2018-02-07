# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
pkgver=0.21.6
pkgrel=2
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools' 'python-setuptools-scm')
depends=('python3')
source=("https://pypi.python.org/packages/b8/22/4e5cff49209da0b95407569a0a447dc7fb75226acf38e98ecf23cbba2f42/lz4-$pkgver.tar.gz")
md5sums=('775f2040423816264bbb9531a00b1a9d')

package() {
  cd $srcdir/lz4-$pkgver
  python3 setup.py install --root=$pkgdir || return 1
}
