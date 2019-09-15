# Maintainer: Mike Sampson <mike at sambodata dot com>
# Contributor: Thomas Zervogiannis <tzervo@gmail.com>
# Contributor: Loui Chang <louipc dot ist at gmail company>
# Contributor: rabyte <rabyte__gmail>

pkgname=tintin
pkgver=2.01.90
pkgrel=1
pkgdesc="A console-based MUD client"
arch=('i686' 'x86_64')
url="http://tintin.sourceforge.net/"
license=('GPL3')
depends=('zlib' 'pcre' 'gnutls')
options=('strip')
source=(http://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver.tar.gz)
sha512sums=('7b495e13937c7ba2e2f33686bffd73dd272d7f3a9355bb5384785fca32aa34edc84a8b81bfe8d252c2cdaec9ac94663a1ff17654e15143dad191da8e9017e626')

build() {
  cd $srcdir/tt/src
  sh configure --prefix=/usr --enable-big5
  make

}

package() {
  cd $srcdir/tt/src
  install -m755 -D tt++ $pkgdir/usr/bin/tt++
  ln -sf tt++ $pkgdir/usr/bin/tintin

}
