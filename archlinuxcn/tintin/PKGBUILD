# Maintainer: Mike Sampson <mike at sambodata dot com>
# Contributor: Thomas Zervogiannis <tzervo@gmail.com>
# Contributor: Loui Chang <louipc dot ist at gmail company>
# Contributor: rabyte <rabyte__gmail>

pkgname=tintin
pkgver=2.02.05
pkgrel=1
pkgdesc="A console-based MUD client"
arch=('i686' 'x86_64')
url="http://tintin.sourceforge.net/"
license=('GPL3')
depends=('zlib' 'pcre' 'gnutls')
options=('strip')
source=(http://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver.tar.gz)
sha512sums=('3eb4bdacf8b4c5898b6d677a28435f9f1b07c5a605fec0439bbbbab486de8b7c90cb2202583f4c087850270d7a43ac45933cc095411bac3b446a7710c1488944')

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
