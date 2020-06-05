# Maintainer: oldherl <oldherl@gmail.com>

pkgname=ttf-myuppy-gb
pkgver=1
pkgrel=1
pkgdesc="MYuppy GB is a free Simplified Chinese font from the Symbian project, designed to appeal to young urban professionals."
url="https://github.com/SymbianSource/oss.FCL.sf.os.textandloc/tree/master/fontservices/referencefonts/truetype"
license=("EPL")
arch=(any)
source=(
"https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/master/fontservices/referencefonts/truetype/MYuppyGB-Medium.ttf"
"https://raw.githubusercontent.com/SymbianSource/oss.FCL.sf.os.textandloc/master/fontservices/referencefonts/truetype/MYuppyGB-Medium_README.TXT"
)
sha256sums=('a5b6d8ab3d098796ef93178b5a384419738f3ac573b6943b2dc11500347be973'
            'f7c2c3b012e870077ef159890f614f83bb430bfd7dde0a77d978ea1e6a677236')

prepare(){
  iconv -f windows-1252 -t utf-8 MYuppyGB-Medium_README.TXT > README
}

package(){
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/doc/${pkgname}"
  install -m644 MYuppyGB-Medium.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 README "$pkgdir/usr/share/doc/${pkgname}/"
} 
