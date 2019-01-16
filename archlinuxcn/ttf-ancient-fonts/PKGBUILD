# Maintainer: Alex Zose <alexander.zosimidis[at]gmail[dot]com>

pkgname=ttf-ancient-fonts
pkgver=2.60
pkgrel=1
pkgdesc="Unicode Fonts for Ancient Scripts"
url="http://users.teilar.gr/~g1951d/"
license=("custom")
arch=(any)
depends=(fontconfig xorg-font-utils)
conflicts=(ttf-symbola)
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${pkgname}_${pkgver}.orig.tar.xz"
        "license")
sha512sums=("5db3577cad65665846d844fda267539885fe25a863ed6ab6bb6408743e7a62da130ce1de02d9d6995afed147644ebdf472d014ac95622d9c65115582385078a8"
            "87d39b299453247786a0705a36589433f5e209111045103899a0ff957d2c72d4017f0c43ad5734381f7040ef77fd3072e2fb36167f9175d055e2fbc173d31d42")

package() {
  install -d "$pkgdir/usr/share/fonts/TTF"
  install -d "$pkgdir/usr/share/fonts/OTF"
  install -d "$pkgdir/usr/share/licenses/${pkgname}"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.ttf "$pkgdir/usr/share/fonts/TTF/"
  install -m644 "$srcdir/${pkgname}-${pkgver}.orig/"*.otf "$pkgdir/usr/share/fonts/OTF/"
  install -m644 "license" "$pkgdir/usr/share/licenses/${pkgname}/license"
} 
