# Maintainer: Alex Zose <alexander.zosimidis[at]gmail[dot]com>

pkgname=ttf-ancient-fonts
pkgver=2.59
pkgrel=1
pkgdesc="Unicode Fonts for Ancient Scripts"
url="http://users.teilar.gr/~g1951d/"
license=("custom")
arch=(any)
depends=(fontconfig xorg-font-utils)
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${pkgname}_${pkgver}.orig.tar.xz"
	"license")
md5sums=("df026a39ad8b6069bda9123c0d35ad27"
	 "01fc16b0f556bf616d486e2190ad3f9f")
install=$pkgname.install

package() {
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/licenses/${pkgname}"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 "license" "$pkgdir/usr/share/licenses/${pkgname}/license"
} 
