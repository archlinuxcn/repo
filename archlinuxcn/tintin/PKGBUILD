# Maintainer: Mike Sampson <mike at sambodata dot com>
# Contributor: Thomas Zervogiannis <tzervo@gmail.com>
# Contributor: Loui Chang <louipc dot ist at gmail company>
# Contributor: rabyte <rabyte__gmail>

pkgname=tintin
pkgver=2.02.10
pkgrel=1
pkgdesc="A console-based MUD client"
arch=('i686' 'x86_64')
url="http://tintin.sourceforge.net/"
license=('GPL3')
depends=('zlib' 'pcre' 'gnutls')
options=('strip')
source=(https://github.com/scandum/tintin/releases/download/$pkgver/tintin-$pkgver.tar.gz)
sha512sums=('fda57f3a206598e68df2c52a2f50b7015f8acf3809986a6bc036bb5571ff7fa76dc9c36a891c9c9f91bc2b84477dbb973911ab5fdbf76bb060f45309ea876b50')

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
