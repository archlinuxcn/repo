# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Elena ``of Valhalla'' Grandi <gmail.com: elena.valhalla>
# Contributor: Jesse Jaara <gmail.com: jesse.jaara>

pkgname=ttf-symbola
pkgver=11.00
pkgrel=3
pkgdesc="Font for unicode symbols (part of Unicode Fonts for Ancient Scripts)."
arch=('any')
conflicts=('ttf-symbola-ib')
provides=('ttf-symbola')
url="http://users.teilar.gr/~g1951d/"
license=('custom')
depends=('fontconfig' 'xorg-font-utils')
makedepends=('unzip')
source=("${pkgname}-${pkgver}.zip::http://users.teilar.gr/~g1951d/Symbola.zip"
        "LICENSE")
sha512sums=('be7b3fd8b2070a6713b189c0ee0c6d8aef481eb0c7e476dabfa3eb1a599cc7f3a00f14d7b9ca1f563722d550c098f272f62bb99fc490aba8132ed5ae7de59a7b'
            '9afe91785611955511248fd31a86c7e370b23b1b2c37f9345c8f274b3e0e1dbf9c0da8f9edac62d27d318e56485b80966aa7622f167f4da5d5925a7935bfa3da')

package() {
  install -Dm644 Symbola.ttf "$pkgdir/usr/share/fonts/TTF/Symbola.ttf"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
