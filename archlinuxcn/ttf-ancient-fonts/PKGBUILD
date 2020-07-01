# Maintainer: Alex Zose <alexander.zosimidis[at]gmail[dot]com>

pkgname=ttf-ancient-fonts
pkgver=2.60
pkgrel=2
pkgdesc="Unicode Fonts for Ancient Scripts"
url="https://dn-works.com/ufas/"
license=("custom")
arch=(any)
conflicts=(ttf-symbola)
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${pkgname}_${pkgver}.orig.tar.xz"
        "license")
sha512sums=("5db3577cad65665846d844fda267539885fe25a863ed6ab6bb6408743e7a62da130ce1de02d9d6995afed147644ebdf472d014ac95622d9c65115582385078a8"
            "873fc80ac7de4938ec257b2f87d4af4b81298f3952278bddccfad8690d4b544462a9961038af79267a1e71aec6a025baaaa71cfa779afeb7562fca11636fe703")

package() {
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/fonts/OTF"
  install -d "$pkgdir/usr/share/licenses/${pkgname}"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.otf "$pkgdir/usr/share/fonts/OTF/"
  install -m644 "license" "$pkgdir/usr/share/licenses/${pkgname}/license"
} 
