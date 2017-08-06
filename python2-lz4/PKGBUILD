# Submitter: Vladimir Tsanev <tsachev@gmail.com>
# Previous Maintainer: Andrew Reed <reed.996@osu.edu>
# Maintainer: "Score_Under" <seejay.11@gmail.com>
pkgname=python2-lz4
pkgver=0.10.1
pkgrel=1
pkgdesc="LZ4 Bindings for Python"
arch=('any')
url="https://github.com/steeve/python-lz4"
license=('BSD')
makedepends=('python2-distribute')
depends=('python2')
source=("https://pypi.python.org/packages/f5/c6/ef2890b5e287735576e15c1389aa0b9032c9d78ed72385fbd1149af593cd/lz4-$pkgver.tar.gz")
md5sums=('1b8de6217e0785e92f457056c053e058')  # Officially provided
sha256sums=('a0423290a6e89c1789525a7e9d344d877c7a97102cf5c0f99b2319ac560f1b3e')

package() {
  cd $srcdir/lz4-$pkgver
  python2 setup.py install --root=$pkgdir || return 1
}
