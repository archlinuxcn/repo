# Maintainer:  Blallo <blallo@autistici.org>

pkgname=ttf-teranoptia-furiae
pkgver=1.0
pkgrel=1
pkgdesc='An illustrative font which allows you to create chimeric creatures.'
arch=('any')
url='https://www.tunera.xyz/fonts/teranoptia'
license=('custom:SIL Open Font License v1.1')
source=("Teranoptia-Furiae-${pkgver}.ttf::https://gitlab.com/arielmartinperez/teranoptia/-/raw/main/fonts/Teranoptia-Furiae.ttf?ref_type=heads&inline=false"
        "LICENSE.txt::https://gitlab.com/arielmartinperez/teranoptia/-/raw/main/LICENSE.txt?ref_type=heads&inline=false")
sha256sums=('b6dcafa0bfeebdfe06963a40af783ce969f68c26ebb82ff3889c1cf064d83587'
            '5f92645f3c8e0f5c3e6fe7945af5e377b1744980b49bff8d2428094a0677ba27')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Teranoptia-Furiae-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Teranoptia-Furiae.ttf"
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
