# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Solomon Choina <shlomochoina@gmail.com>
# Contributor: Morten Linderud <foxboron@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Elena ``of Valhalla'' Grandi <gmail.com: elena.valhalla>
# Contributor: Jesse Jaara <gmail.com: jesse.jaara>
# Contributor: bohoomil <@zoho.com>

pkgbase=font-symbola
pkgname=('otf-symbola' 'ttf-symbola')
pkgver=13.00
pkgrel=8
pkgdesc='Font for symbol blocks of the Unicode Standard'
arch=('any')
url='https://dn-works.com/ufas/'
license=('custom')
makedepends=('fontforge' 'poppler')
source=("$pkgbase-$pkgver-$pkgrel.zip::https://dn-works.com/wp-content/uploads/2020/UFAS-Fonts/Symbola.zip"
        "License-$pkgver-$pkgrel.pdf::https://dn-works.com/wp-content/uploads/2020/UFAS-Docs/License.pdf")
sha512sums=('ba671168ab2dc15293ae404f849f13b9b1f4684ce1856a8c2bbf8b9a2e2d70a27f86ef166a5e3ab6260e651c8276537ee272710a7e1fb49beef26fbed6355a35'
            '6b6f7688a5571375b59135e2a60c61d0ad7fd2d19f0f226a38b8b39696c6f01047758937e9431f8d64f4758fe207eac83ba4df847efccb24b119be4aff69dbf3')

build() {
  fontforge -c 'open(argv[1]).generate(argv[2])' Symbola.{otf,ttf}
  pdftotext "${source[1]%::*}" LICENSE
}

package_otf-symbola() {
  provides=('font-symbola')
  pkgdesc+=' (OTF)'
  install -Dm644 -t "$pkgdir/usr/share/fonts/OTF/" Symbola.otf
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}

package_ttf-symbola() {
  conflicts=('ttf-symbola-ib<=13.00')
  provides=('font-symbola')
  pkgdesc+=' (TTF)'
  install -Dm644 -t "$pkgdir/usr/share/fonts/TTF/" Symbola.ttf
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
