# Maintainer: Max Chesterfield <`echo Y2hlc3RtMDA3QGhvdG1haWwuY29tCg== | base64 -d`>


pkgname=cqlsh
pkgdesc="CQL shell for apache cassandra"
pkgver=3.11.4
pkgrel=1
arch=('any')
license=('Apache')
depends=('python2' 'python2-cassandra-driver-git')
makedepends=('python2-setuptools' 'cython2')
url="https://github.com/apache/cassandra"
source=("git+https://github.com/apache/cassandra/#tag=cassandra-$pkgver")
md5sums=('SKIP')

build() {
  cd "$srcdir/cassandra/pylib"
  python2 setup.py build
}

package() {
  mkdir -p $pkgdir/usr/bin
  cp "$srcdir/cassandra/bin/cqlsh" $pkgdir/usr/bin/cqlsh
  cp "$srcdir/cassandra/bin/cqlsh.py" $pkgdir/usr/bin/cqlsh

  cd "$srcdir/cassandra/pylib"
  python2 setup.py install --prefix=/usr --root="$pkgdir"
} 
