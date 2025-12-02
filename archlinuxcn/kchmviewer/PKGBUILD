# Maintainer: Andreas Baumann <mail@andreasbaumann.cc>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Alexander Bogdanov <andorn@gmail.com>

pkgname=kchmviewer
pkgver=8.0
pkgrel=8
pkgdesc="A .chm files (MS HTML help file format) viewer"
arch=('x86_64')
url="http://kchmviewer.sourceforge.net/"
license=('GPL-3.0-or-later')
depends=('chmlib' 'libzip' 'qt5-webengine')
makedepends=('qt5-base')
changelog=$pkgname.changelog
source=($pkgname-$pkgver.tar.gz::https://github.com/gyunaev/$pkgname/archive/refs/tags/RELEASE_8_0.tar.gz
       $pkgname-$pkgver-url-scheme.patch::https://github.com/gyunaev/$pkgname/commit/9ac73e7ad15de08aab6b1198115be2eb44da7afe.patch
       $pkgname-$pkgver-no-webkit.patch::https://github.com/gyunaev/$pkgname/commit/a4a3984465cb635822953350c571950ae726b539.patch
       $pkgname-$pkgver-fix-8.0-build.patch::https://github.com/gyunaev/$pkgname/commit/e3b09edbbae17ad19661a7514afe5a9d84ca0ffa.patch
       $pkgname-$pkgver-qtwebengine.patch::https://github.com/gyunaev/$pkgname/commit/99a6d94bdfce9c4578cce82707e71863a71d1453.patch)
sha256sums=('0eec144b2c09c8b6be98b795f84767098c893bdad7b5a3d11fc5faafead5f9b2'
            '982026d08f1ae9d77ff8fcb3a6e3b14a4c473461362517ac8ab6d13f8a75f116'
            '9c93744dd0ee02f0004a196499bb90c32aee67daf6efc7c104dd6714ae12f983'
            '9a3022ce78ab97b6816f80b04557dc25c5dde868e6d89a2a2435ce51417b4f2c'
            '5689a4753d895fc3060e1068c041c45784c079f75739593946ef8860940756b7')

prepare() {
  cd $pkgname-RELEASE_8_0
  
#https://github.com/gyunaev/kchmviewer/issues/10
  patch -Np1 -i "${srcdir}"/$pkgname-$pkgver-url-scheme.patch


#remove unused webkit
  patch -Np1 -i "${srcdir}"/$pkgname-$pkgver-no-webkit.patch

#https://github.com/gyunaev/kchmviewer/issues/9
  patch -Np1 -i "${srcdir}"/$pkgname-$pkgver-fix-8.0-build.patch

#https://github.com/gyunaev/kchmviewer/pull/13
  patch -Np1 -i "${srcdir}"/$pkgname-$pkgver-qtwebengine.patch

}

build() {
  cd $pkgname-RELEASE_8_0

  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd $pkgname-RELEASE_8_0

  make DESTDIR="${pkgdir}" install

  install -Dm755 bin/$pkgname "${pkgdir}"/usr/bin/$pkgname
#icon/desktop file
  install -Dm644 packages/$pkgname.png "${pkgdir}"/usr/share/pixmaps/$pkgname.png
  install -Dm644 packages/$pkgname.desktop "${pkgdir}"/usr/share/applications/$pkgname.desktop
}
