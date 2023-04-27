# Maintainer: not_anonymous <nmlibertarian@gmail.com>
# Original Contributor: Bob Finch <w9ya@qrparci.net>

pkgname=hamradio-menus
pkgver=1.0
pkgrel=2
pkgdesc="Ham radio (specific) XDG-compliant menu"
arch=('any')
url="http://www.archlinux.org/"
license=(GPL)
depends=('desktop-file-utils')
install=$pkgname.install
source=(hamradio.png
	HamRadio.directory
        hamradio.menu)

package() {
  cd $srcdir

  mkdir -p $pkgdir/usr/share/desktop-directories
  mkdir -p $pkgdir/usr/share/pixmaps/hamradio
  mkdir -p $pkgdir/etc/xdg/menus/applications-merged
  mkdir -p $pkgdir/etc/xdg/menus/kde-applications-merged

  install -m644 *.directory $pkgdir/usr/share/desktop-directories/
  install -m644 *.png $pkgdir/usr/share/pixmaps/hamradio
  install -m644 *.menu $pkgdir/etc/xdg/menus/applications-merged/
  install -m644 *.menu $pkgdir/etc/xdg/menus/kde-applications-merged/
}
md5sums=('b24ce93a15cca693efa662ab90ae0fda'
         '7c81ee375134d8e5ab7bfbbfd69098f7'
         '8ae4d78b8bacf823eecf81f064e43c91')
sha256sums=('e55aabbf91ad110672d87290582705a55c6a52bb5b487c7bd195f5e18cc550b3'
            '4bcaaa1ca3f7e0d31aac3cf51399f0a1c6ac0c1192231e8311f00cf688ad977a'
            'd9a8c97b934e19e0c3a7be03664eb892390dc5f978180f7b924a30a481ec66e2')
