# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
pkgname=vimix-cursors
_pkgname=Vimix-cursors
_pkgver=2020-02-24
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="An X Cursor theme inspired by Material design and based on capitaine-cursors"
arch=('any')
url="https://github.com/vinceliuice/Vimix-cursors"
license=('GPL3')
source=("$_pkgname-$_pkgver.tar.gz::$url/archive/$_pkgver.tar.gz")
options=('!strip')
sha256sums=('69298d02264b5b15239c340f8fa899f91574c0eac49ad5745e8e588315423618')

package() {
  cd "$_pkgname-$_pkgver"
  install -d "$pkgdir"/usr/share/icons/{"$_pkgname",Vimix-white-cursors}
  cp -dr --no-preserve=ownership dist/* "$pkgdir/usr/share/icons/$_pkgname"
  cp -dr --no-preserve=ownership dist-white/* "$pkgdir/usr/share/icons/Vimix-white-cursors"
}
