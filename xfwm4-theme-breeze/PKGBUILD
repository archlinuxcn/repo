# Maintainer: twa022 <twa022 at gmail dot com>

pkgname="xfwm4-theme-breeze"
pkgver=0.1.0
pkgrel=1
url="https://github.com/psy-q/xfwm-theme-breeze"
#url="https://www.xfce-look.org/content/show.php/Breeze-xfwm?content=171330"
pkgdesc="Xfce theme to Plasma 5's Breeze theme."
arch=('any')
license=('GPL2')
depends=('xfwm4')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('0e7612a36664033cb087c99fd74d8c44f87e7afec3808f1fdeba204d6e1d54d2')

package() {
	mkdir -p "$pkgdir"/usr/share/themes/
	cp -ar --no-preserve=ownership "$srcdir"/xfwm-theme-breeze-0.1.0 "$pkgdir"/usr/share/themes/xfwm-theme-breeze
}
