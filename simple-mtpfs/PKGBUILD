# Maintainer: goetzc
# Contributor: Dan Liew <dan at su-root dot co dot uk>
pkgname=simple-mtpfs
pkgver=0.3.0
pkgrel=1
pkgdesc="A FUSE filesystem that supports reading/writing from MTP devices"
arch=('i686' 'x86_64')
url="https://github.com/phatina/simple-mtpfs/"
license=('GPL2')
depends=('libmtp' 'fuse' 'gcc-libs')
source=(https://github.com/phatina/simple-mtpfs/archive/$pkgname-$pkgver.tar.gz)
sha1sums=('9bbb315a4cc1020cdffbfea969dbd3c7a364c42d')

build() {
  cd "$srcdir/$pkgname-$pkgname-$pkgver"
  if [[ ! -e "./configure" ]]; then 
    ./autogen.sh 
    ./configure --prefix=/usr
  else
    ./config.status
  fi
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}
