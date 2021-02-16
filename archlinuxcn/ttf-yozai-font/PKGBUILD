# Maintainer: oldherl <oldherl@gmail.com>

pkgname=ttf-yozai-font
pkgver=0.850
pkgrel=1
pkgdesc="Handwritten-style Chinese font derived from Y.OzFont."
url="https://github.com/lxgw/yozai-font"
license=("custom:OFL")
arch=(any)
source=(
"$pkgname"::'git+https://github.com/lxgw/yozai-font.git#commit=dff6560b55203cde1c21babcd05997c28a69172d'
)
sha256sums=("SKIP")

package(){
  cd "$srcdir/$pkgname"
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/doc/${pkgname}"
  install -d "$pkgdir/usr/share/licenses/${pkgname}"
  install -m644 ttf/*.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 README.md "$pkgdir/usr/share/doc/${pkgname}/"
  install -m644 SIL_Open_Font_License_1.1.txt "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
} 
