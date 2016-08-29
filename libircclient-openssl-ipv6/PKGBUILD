# Maintainer:  Shengyu Zhang <lastavengers@outlook.com>
# Contributor: speps <speps at aur dot archlinux dot org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Marcel Wysocki <maci@satgnu.net>
# Contributor: coolkehon <coolkehon at g m a i l>

pkgname=libircclient-openssl-ipv6
_pkgname=libircclient
pkgver=1.9
pkgrel=2
pkgdesc='Small but powerful library, which implements client-server IRC protocol, with openSSL and ipv6 support'
arch=('i686' 'x86_64')
url='http://www.ulduzsoft.com/libircclient/'
license=('GPL')
depends=('glibc' 'openssl')
makedepends=('python2-sphinx' 'python2-rst2pdf') 
source=("http://downloads.sourceforge.net/sourceforge/$_pkgname/$_pkgname-$pkgver.tar.gz")
md5sums=('783c48fe9153ed55a5565c818a178d67')
conflicts=('libircclient')
provides=('libircclient')
prepare() {
  cd $_pkgname-$pkgver/src

  # fix include dir path
  sed -i "s/@\/include/&\/$_pkgname/" Makefile.in
}

build() {
  cd $_pkgname-$pkgver
  ./configure --prefix=/usr \
              --libdir=/usr/lib \
              --enable-shared \
              --enable-openssl \
              --enable-ipv6
  cd src && make

  cd ../doc
  make SPHINXBUILD=sphinx-build2 singlehtml man
}

package() {
  cd $_pkgname-$pkgver/src
  make DESTDIR="$pkgdir" install

  # docs
  install -d "$pkgdir/usr/share/doc/$_pkgname"
  cp -a ../doc/_build/singlehtml/* "$pkgdir/usr/share/doc/$_pkgname"

  # man
  install -Dm644 ../doc/_build/man/$_pkgname.1 \
    "$pkgdir/usr/share/man/man1/$_pkgname.1"

  # examples
  install -d "$pkgdir/usr/share/$_pkgname/examples"
  install -Dm644 ../examples/* \
    "$pkgdir"/usr/share/$_pkgname/examples
}
