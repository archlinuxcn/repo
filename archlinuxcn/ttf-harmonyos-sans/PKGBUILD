# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=ttf-harmonyos-sans
_pkgname='HarmonyOS Sans'
pkgver=2025.06.21
pkgrel=1
pkgdesc="HarmonyOS Sans Fonts.华为鸿蒙字体"
arch=("any")
url="https://developer.huawei.com/consumer/cn/design/resource/"
license=("LicenseRef-custom")
conflicts=("${pkgname//ttf-/}")
source=(
    "${pkgname}-${pkgver}.zip::https://developer.huawei.com/images/download/next/${_pkgname// /-}-v3.zip"
)
sha256sums=('475613cc1f99205a4371493ddb9cdf88446e01d09561fd01ffdec2dc406e8d18')
package() {
    export LC_CTYPE="zh_CN.UTF-8"
    find "${srcdir}/${_pkgname}" -type f -name "*.ttf" -exec install -Dm644 -t "${pkgdir}/usr/share/fonts/${pkgname//ttf-/}" {} +
}