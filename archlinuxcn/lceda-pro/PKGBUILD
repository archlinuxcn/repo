# Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Misaka13514 <Misaka13514 at gmail dot com>

pkgbase=lceda-pro
pkgname=lceda-pro
pkgver=2.0.17
pkgrel=1
pkgdesc="免费、专业、强大的国产PCB设计工具"
arch=('x86_64' 'aarch64' 'loong64')
url="https://pro.lceda.cn/"
license=('custom')
depends=(gtk3 nss alsa-lib electron libappindicator-gtk3 libnotify)
install=${pkgname}.install
source=("LICENSE"
        "${pkgname}.install")
source_x86_64=("${pkgname}-x86_64-${pkgver}.zip::https://image.lceda.cn/files/lceda-pro-linux-x64-${pkgver}.zip")
source_aarch64=("${pkgname}-aarch64-${pkgver}.zip::https://image.lceda.cn/files/lceda-pro-linux-arm64-${pkgver}.zip")
source_loong64=("${pkgname}-loong64-${pkgver}.zip::https://image.lceda.cn/files/lceda-pro-linux-loong64-${pkgver}.zip")
sha256sums=('9b53bc19a98498c86019cc32a3ade6ad0ee4b12ba30686feb93132a5f0da52f5'
            'f8c3c7f65443801b8a70e40de7cdceade5dcd75974945695dd5a1bfb1f862e1a')
sha256sums_x86_64=('22a23cf3a59ddf988f789d9a4e6d993ba501998b347a5c1f56821fb8a152e5fd')
sha256sums_aarch64=('099d78c24f1b483207ad869e51daf1435a94504f9d01e23bd1ef7c32d12d0bb3')
sha256sums_loong64=('d6e2f8e256a5bcccd3b38097f008b7f3d02cf007ff0247e3d5e9f2d46a164a34')

package() {
    export LC_CTYPE="zh_CN.UTF-8"

    # electron file
    install -dm0755 "${pkgdir}/usr/lib/${pkgname}/"

    cd ${srcdir}/${pkgname}/
    cp -r resources ${pkgdir}/usr/lib/${pkgname}

    # icon
    local _icon
    for _icon in 16 32 64 128 256 512; do
        install -Dm0644 icon/icon_${_icon}x${_icon}.png \
                        ${pkgdir}/usr/share/icons/hicolor/${_icon}x${_icon}/apps/${pkgname}.png
    done
    install -Dm644 icon/icon_512x512@2x.png \
                   ${pkgdir}/usr/share/icons/hicolor/1024x1024/apps/${pkgname}.png

    # desktop entry
    install -Dm0644 lceda-pro.dkt \
                    ${pkgdir}/usr/share/applications/${pkgname}.desktop

    sed -i 's|/opt/lceda-pro/icon/icon_128x128.png|lceda-pro|g' \
        ${pkgdir}/usr/share/applications/${pkgname}.desktop
    sed -i 's|/opt/lceda-pro/||g' \
        ${pkgdir}/usr/share/applications/${pkgname}.desktop

    # lceda-pro file
    install -Dm0755 /dev/stdin ${pkgdir}/usr/bin/${pkgname} << EOF
#!/bin/sh

exec electron /usr/lib/lceda-pro/resources/app/ "\$@"
EOF
    # LICENSE
    install -Dm0644 ${srcdir}/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    install -Dm0644 LCEDA-Distribution-License.txt ${pkgdir}/usr/share/licenses/${pkgname}/LCEDA-DLA.txt
}
