pkgname=log4cxx
pkgver=0.10.0
pkgrel=4
pkgdesc="A C++ port of Log4j"
url="http://logging.apache.org/log4cxx"
license=("Apache")
depends=('apr-util' 'libxml2')
arch=('any')
makedepends=('autoconf' 'automake' 'libtool' 'patch' 'zip' 'gzip' 'sed')
provides=('log4cxx')
conflicts=('log4cxx-svn')

source=("http://archive.apache.org/dist/logging/$pkgname/$pkgver/apache-$pkgname-$pkgver.tar.gz"
        'log4cxx-0.10.0-missing_includes.patch'
        'log4cxx-0.10.0-narrowing-fixes-from-upstream.patch')
sha512sums=('1c34d80983db5648bc4582ddcf6b4fdefdc6594c2769f95235f5441cd6d03cf279cc8f365e9a687085b113f79ebac9d7d33a54b6aa3b3b808c0e1a56a15ffa37'
            '14fa0b19516171cbbe2c6220816819fc52cf8f3b3ded5d71966e2f4a71bda9ce1ed8fe7e57745a835e6ac5558631916ed9824d09ec7469d84c7bf99fb4946304'
            '15b692b37961adbc808e4c10d2719483502f3ac060ee5be248832d4e2a2f76f7d9e120ea9a6bf908230cf230a893964040e54415cca35a12e576d0a5ab1f4176')

build() {
  cd "$srcdir/apache-$pkgname-$pkgver"

  patch -p1 < $startdir/log4cxx-0.10.0-missing_includes.patch
  patch -p1 < $startdir/log4cxx-0.10.0-narrowing-fixes-from-upstream.patch

  #./autogen.sh
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd "$srcdir/apache-$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}
