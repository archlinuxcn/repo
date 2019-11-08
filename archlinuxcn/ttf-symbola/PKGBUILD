# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Elena ``of Valhalla'' Grandi <gmail.com: elena.valhalla>
# Contributor: Jesse Jaara <gmail.com: jesse.jaara>

pkgname=ttf-symbola
pkgver=12.00
pkgrel=2
pkgdesc="Font for unicode symbols (part of Unicode Fonts for Ancient Scripts)."
arch=('any')
conflicts=('ttf-symbola-ib')
provides=('ttf-symbola')
url="http://users.teilar.gr/~g1951d/"
license=('custom')
depends=('fontconfig' 'xorg-font-utils')
source=("${pkgname}-${pkgver}.zip::http://users.teilar.gr/~g1951d/Symbola.zip"
        "LICENSE")
sha512sums=('96057c9dbf8a1ab48323d49f727dc00eb8ab66a60e4037b622280d6b84a2c692129e174994a36683ba78bee43e2a2096c4d87ac5c350be78f4d8d6cd7218a528'
            '9afe91785611955511248fd31a86c7e370b23b1b2c37f9345c8f274b3e0e1dbf9c0da8f9edac62d27d318e56485b80966aa7622f167f4da5d5925a7935bfa3da')

package() {
  install -Dm644 Symbola.ttf "$pkgdir/usr/share/fonts/TTF/Symbola.ttf"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
