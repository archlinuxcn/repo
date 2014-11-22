# Maintainer: birdflesh <antkoul at gmail dot com>
# Contributor: Army <uli.armbruster@gmail.com>
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: dale <dale@archlinux.org>

pkgname=ttf-ms-fonts
pkgver=2.0
pkgrel=10
pkgdesc="Core TTF Fonts from Microsoft"
arch=('any')
url="http://corefonts.sourceforge.net/"
license=('custom:microsoft')
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
makedepends=('libarchive>=3.0.2')
provides=('ttf-font')
install=$pkgname.install
_sfpath="http://downloads.sourceforge.net/corefonts"
source=($_sfpath/andale32.exe $_sfpath/arial32.exe  $_sfpath/arialb32.exe
        $_sfpath/comic32.exe  $_sfpath/courie32.exe $_sfpath/georgi32.exe
        $_sfpath/impact32.exe $_sfpath/times32.exe  $_sfpath/trebuc32.exe
        $_sfpath/verdan32.exe $_sfpath/webdin32.exe)
md5sums=('cbdc2fdd7d2ed0832795e86a8b9ee19a'
         '9637df0e91703179f0723ec095a36cb5'
         'c9089ae0c3b3d0d8c4b0a95979bb9ff0'
         '2b30de40bb5e803a0452c7715fc835d1'
         '4e412c772294403ab62fb2d247d85c60'
         '4d90016026e2da447593b41a8d8fa8bd'
         '7907c7dd6684e9bade91cff82683d9d7'
         'ed39c8ef91b9fb80f76f702568291bd5'
         '0d7ea16cac6261f8513a061fbfcdb2b5'
         '12d2a75f8156e10607be1eaa8e8ef120'
         '230a1d13a365b22815f502eb24d9149b')

package() { 
  install -dm755 "$pkgdir/usr/share/fonts/TTF"

  for font in *.{ttf,TTF}; do
    install -m644 $font "$pkgdir/usr/share/fonts/TTF/$(echo $font|tr A-Z a-z)"
  done

  install -Dm644 Licen.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
