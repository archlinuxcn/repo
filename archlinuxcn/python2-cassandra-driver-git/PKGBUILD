# Maintainer: Max Chesterfield <`echo Y2hlc3RtMDA3QGhvdG1haWwuY29tCg== | base64 -d`>


pkgname=python2-cassandra-driver-git
pkgdesc="DataStax Python Driver for Apache Cassandra"
pkgver=3.17.0
provides=('python2-cassandra-driver')
pkgrel=1
arch=('any')
license=('Apache')
depends=('python2' 'python2-six' 'python2-futures')
makedepends=('python2-setuptools' 'libev')
url="https://github.com/datastax/python-driver"
source=("git+https://github.com/datastax/python-driver#tag=$pkgver")
md5sums=('SKIP')

build() {
  cd "$srcdir/python-driver"
  CASS_DRIVER_BUILD_CONCURRENCY=$(nproc) python2 setup.py build
}

package() {
  cd "$srcdir/python-driver"
  python2 setup.py install --prefix=/usr --root="$pkgdir"
} 
