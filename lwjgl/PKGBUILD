# Maintainer: Frederik "Freso" S. Olesen <freso.dk@gmail.com>
pkgname=lwjgl
pkgver=3.0.0a
pkgrel=1
pkgdesc='Lightweight Java Game Library - for use in game projects in Java.'
arch=(any)
url='http://lwjgl.org/'
license=('BSD')
changelog=ChangeLog
options=(!strip)
source=(http://build.lwjgl.org/release/$pkgver/$pkgname-$pkgver.zip)
md5sums=('3198c644b983c20534d58cf2d8e3f029')
sha1sums=('baa3bb9ac71040c675ba717198a424e7c086c90e')

package() {
  _sharedir="$pkgdir/usr/share"
  # Install licenses
  install -d $_sharedir/licenses/$pkgname/3rdparty
  install -m644 -t $_sharedir/licenses/$pkgname/3rdparty doc/3rdparty/*
  install -m644 -t $_sharedir/licenses/$pkgname doc/LICENSE.txt
  rm -rf doc/LICENSE.txt doc/3rdparty
  # Install docs
  install -d $_sharedir/doc/$pkgname
  install -m644 -t $_sharedir/doc/$pkgname doc/*
  # Install library files
  install -d $_sharedir/$pkgname/jar
  install -m644 -t $_sharedir/$pkgname/jar jar/*
  install -d $_sharedir/$pkgname/native
  install -m644 -t $_sharedir/$pkgname/native native/*
  install -m644 -t $_sharedir/$pkgname build.txt src.zip
}

# vim:set ts=2 sw=2 et:
