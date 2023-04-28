# Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Misaka13514 <Misaka13514 at gmail dot com>

pkgbase=lceda-pro
pkgname=lceda-pro
pkgver=2.0.21
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
sha256sums_x86_64=('64a3e9595fe54f6467bb015b5bc3a5ae73109f0e39fc7b91fcb1536d1fdc8a52')
sha256sums_aarch64=('3ee36eb676b2e9a8cc0e1a46403d976c7948fa790f820960eca2087656c2c40c')
sha256sums_loong64=('e4b054ad52708bb9350e88c9eb09e16a06fb7a67117df7ac47cefd76be8166f5')

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
