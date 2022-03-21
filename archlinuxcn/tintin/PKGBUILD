# Maintainer: Mike Sampson <mike at sambodata dot com>
# Contributor: Thomas Zervogiannis <tzervo@gmail.com>
# Contributor: Loui Chang <louipc dot ist at gmail company>
# Contributor: rabyte <rabyte__gmail>

pkgname=tintin
pkgver=2.02.20
pkgrel=1
pkgdesc="A console-based MUD client"
arch=('i686' 'x86_64')
url="http://tintin.sourceforge.net/"
license=('GPL3')
depends=('zlib' 'pcre' 'gnutls')
options=('strip')
source=(https://github.com/scandum/tintin/releases/download/$pkgver/tintin-$pkgver.tar.gz)
sha512sums=('41e46f55bf88bee58638d1628edda338b9fbbd0197c67dfa8b0610ea58aacdd1039f36e9c3393bc34599a506278538c8782c0ea09ef1fadb6dc6db203bbe359d')

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
