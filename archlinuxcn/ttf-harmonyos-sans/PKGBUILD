# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=ttf-harmonyos-sans
_pkgname="HarmonyOS Sans"
pkgver=2024.06.19
pkgrel=1
pkgdesc="HarmonyOS Sans 字体"
arch=("any")
url='https://developer.harmonyos.com/cn/design/resource'
license=("LicenseRef-custom")
conflicts=("${pkgname//ttf-/}")
source=(
    "${pkgname}-${pkgver}.zip::https://developer.huawei.com/images/download/next/${_pkgname// /-}.zip"
)
sha256sums=('c8ac95f3715631f3787336e9689571c12ae818a0059713a726313605ce0eb8d3')
package() {
    export LC_CTYPE="zh_CN.UTF-8"   
    install -Dm644 "${srcdir}/${_pkgname} /${_pkgname// /_}"*/*.ttf -t "${pkgdir}/usr/share/fonts/${pkgname//ttf-/}"
    install -Dm644 "${srcdir}/${_pkgname} /${_pkgname// /_}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}