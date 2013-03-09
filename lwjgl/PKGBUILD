# Maintainer: Frederik "Freso" S. Olesen <freso.dk@gmail.com>
pkgname=lwjgl
pkgver=2.8.5
pkgrel=1
pkgdesc='Lightweight Java Game Library - for use in game projects in Java.'
arch=(any)
url='http://lwjgl.org/'
license=('BSD')
changelog=ChangeLog
options=(!strip)
source=(http://downloads.sourceforge.net/java-game-lib/$pkgname-$pkgver.zip)
md5sums=('1e08ec6ac655599560a3bbecdee2a11d')
sha1sums=('615937bea17532d953c812ae60dbbe561337187f')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  _sharedir="$pkgdir/usr/share"
  # Install licenses
  install -d $_sharedir/licenses/$pkgname/3rdparty
  install -m644 -t $_sharedir/licenses/$pkgname/3rdparty doc/3rdparty/*
  install -m644 -t $_sharedir/licenses/$pkgname doc/LICENSE
  rm -rf doc/LICENSE doc/3rdparty
  # Install docs
  install -d $_sharedir/doc/$pkgname
  install -m644 -t $_sharedir/doc/$pkgname doc/*
  rm -rf doc
  # Install library files
  install -d $_sharedir/$pkgname
  mv * $_sharedir/$pkgname
}

# vim:set ts=2 sw=2 et:
