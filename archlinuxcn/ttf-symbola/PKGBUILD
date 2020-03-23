# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Elena ``of Valhalla'' Grandi <gmail.com: elena.valhalla>
# Contributor: Jesse Jaara <gmail.com: jesse.jaara>

pkgname=ttf-symbola
pkgver=13.00
pkgrel=1
pkgdesc="Font for unicode symbols (part of Unicode Fonts for Ancient Scripts)."
arch=('any')
conflicts=('ttf-symbola-ib')
provides=('ttf-symbola')
url="https://dn-works.com/ufas/"
license=('custom')
makedepends=('fontforge' 'poppler')
source=("${pkgname}-${pkgver}.zip::https://dn-works.com/wp-content/uploads/2020/UFAS-Fonts/Symbola.zip"
        "LICENSE.pdf::https://dn-works.com/wp-content/uploads/2020/UFAS-Docs/License.pdf")
sha512sums=('57f1c72d9fe03da68fee476f6c3d202805ba5eacfb4690ca5e3b10d4d335cbefaebd501f77af28abc2a71cd34a926a79d633689ff8cb54e972d09b5292f5c8b1'
            '6b6f7688a5571375b59135e2a60c61d0ad7fd2d19f0f226a38b8b39696c6f01047758937e9431f8d64f4758fe207eac83ba4df847efccb24b119be4aff69dbf3')

build() {
  fontforge -c 'open(argv[1]).generate(argv[2])' Symbola.otf Symbola.ttf
  pdftotext LICENSE.pdf LICENSE
}

package() {
  install -Dm644 -t "$pkgdir/usr/share/fonts/TTF/" Symbola.ttf
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
