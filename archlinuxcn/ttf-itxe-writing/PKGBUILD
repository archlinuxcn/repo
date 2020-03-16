# Maintainer: Patrick Young <16604643+kmahyyg@users.noreply.github.com>

pkgname=ttf-itxe-writing
pkgver=1.1
pkgrel=1
_reltag='v20200315'
pkgdesc='A beautiful and elegant hand-writing fonts by ITXE Studio'
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
arch=('any')
url="https://fonts.idc.moe"
license=('custom:ITXE Custom Font License v1.1')
source=(
    "ITXEWriting-${pkgver}.ttf::https://github.com/kmahyyg/personal_pkgbuild/releases/download/${_reltag}/ITXEWriting-${pkgver}.ttf"
    "${pkgname}-${pkgver}-CFL.txt::https://github.com/kmahyyg/personal_pkgbuild/raw/master/${pkgname}/${pkgname}-${pkgver}-CFL.txt"
)
sha256sums=(
    '2427dccaf86980f73f524fc4705f3a00b2cac6228abecae79eb513093a56f2d0'
    'fd2df7ff9d7ffa701c9ab3db634f713ca11181e08fe6f2c113a40fabd6fce803'
)
package() {
    install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
    install -m 644 ITXEWriting-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/ITXEWriting.ttf"
    install -Dm644 ${pkgname}-${pkgver}-CFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
