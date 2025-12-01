pkgbase=ttf-adobe-source-han-serif-cjk-variables
pkgname=(ttf-adobe-source-han-serif-{cn,hk,tw,jp,kr}-variables)
pkgver=2.003R
pkgrel=1
url="https://github.com/adobe-fonts/source-han-serif"
license=('OFL-1.1')
arch=("any")
options=(!debug)
source=("https://github.com/adobe-fonts/source-han-serif/releases/download/$pkgver/02_SourceHanSerif-VF.zip")
sha256sums=('86608d4c1162f80a2f2605a70d3f2072764609598271ee38eb24ea1eaa22dac8')

package_ttf-adobe-source-han-serif-cn-variables() {
    pkgdesc="Adobe Source Han Serif Subset TTF - Simplified Chinese TrueType fonts"

    install -Dm644 "$srcdir"/Variable/TTF/Subset/SourceHanSerifCN-VF.ttf -t "$pkgdir"/usr/share/fonts/adobe-source-han
    install -vDm644 "${srcdir}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_ttf-adobe-source-han-serif-hk-variables() {
    pkgdesc="Adobe Source Han Serif Subset TTF - Traditional Chinese (Hong Kong) TrueType fonts"

    install -Dm644 "$srcdir"/Variable/TTF/Subset/SourceHanSerifHK-VF.ttf -t "$pkgdir"/usr/share/fonts/adobe-source-han
    install -vDm644 "${srcdir}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_ttf-adobe-source-han-serif-tw-variables() {
    pkgdesc="Adobe Source Han Serif Subset TTF - Traditional Chinese (Taiwan) Chinese TrueType fonts"

    install -Dm644 "$srcdir"/Variable/TTF/Subset/SourceHanSerifTW-VF.ttf -t "$pkgdir"/usr/share/fonts/adobe-source-han
    install -vDm644 "${srcdir}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_ttf-adobe-source-han-serif-jp-variables() {
    pkgdesc="Adobe Source Han Serif Subset TTF - Japanese TrueType fonts"

    install -Dm644 "$srcdir"/Variable/TTF/Subset/SourceHanSerifJP-VF.ttf -t "$pkgdir"/usr/share/fonts/adobe-source-han
    install -vDm644 "${srcdir}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_ttf-adobe-source-han-serif-kr-variables() {
    pkgdesc="Adobe Source Han Serif Subset TTF - Korean TrueType fonts"

    install -Dm644 "$srcdir"/Variable/TTF/Subset/SourceHanSerifKR-VF.ttf -t "$pkgdir"/usr/share/fonts/adobe-source-han
    install -vDm644 "${srcdir}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
