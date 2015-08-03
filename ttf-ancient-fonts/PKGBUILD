# Maintainer: Alex Zose <alexander.zosimidis[at]gmail[dot]com>

pkgname=ttf-ancient-fonts
pkgver=2.57
pkgrel=1
pkgdesc="Unicode Fonts for Ancient Scripts"
url="http://users.teilar.gr/~g1951d/"
license=("custom")
arch=(any)
depends=(fontconfig xorg-font-utils)
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${pkgname}_${pkgver}.orig.tar.gz"
	"license")
md5sums=("ee28043d8454f31c6bffc84e55acd823"
	 "91258f5635a1c122f522a1330cd61bbf")
install=$pkgname.install

package() {
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/licenses/${pkgname}"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 "license" "$pkgdir/usr/share/licenses/${pkgname}/license"
} 
