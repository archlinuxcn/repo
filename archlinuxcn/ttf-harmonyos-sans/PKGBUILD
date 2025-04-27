# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=ttf-harmonyos-sans
_pkgname='HarmonyOS Sans'
pkgver=2024.06.19
pkgrel=3
pkgdesc="HarmonyOS Sans Fonts.华为鸿蒙字体"
arch=("any")
url="https://developer.huawei.com/consumer/cn/design/resource/"
license=("LicenseRef-custom")
conflicts=("${pkgname//ttf-/}")
source=(
    "${pkgname}-${pkgver}.zip::https://developer.huawei.com/images/download/next/${_pkgname// /-}-v2.zip"
)
sha256sums=('ba7ddf71fc4dee33a7170869564ad76d421a2ed5c58e5aac9a573c39945ef654')
package() {
    export LC_CTYPE="zh_CN.UTF-8"
    find "${srcdir}/${_pkgname}" -type f -name "*.ttf" -exec install -Dm644 -t "${pkgdir}/usr/share/fonts/${pkgname//ttf-/}" {} +
}