# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
pkgver=0.11.1
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools')
depends=('python3')
source=("https://pypi.python.org/packages/3c/00/668df8820cfafe54257a1e2e723c9bfcd1bd88f5ffe250b6fc6c0cef0fd1/lz4-$pkgver.tar.gz")
md5sums=('2a7d1d8669046c380ad69dbd9db4db94')

package() {
  cd $srcdir/lz4-$pkgver
  python3 setup.py install --root=$pkgdir || return 1
}
