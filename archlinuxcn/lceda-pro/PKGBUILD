# Maintainer: taotieren <admin@taotieren.com>
# Co-Maintainer: Misaka13514 <Misaka13514 at gmail dot com>

pkgname=lceda-pro
pkgver=2.2.42.2
pkgrel=1
pkgdesc="免费、专业、强大的国产PCB设计工具"
arch=(x86_64)
url="https://pro.lceda.cn/"
license=(LicenseRef-LCEDA-Proprietary)
depends=(alsa-lib
         bash
         coreutils
         electron
         gcc-libs
         glibc
         gtk3
         hicolor-icon-theme
         libpulse
         nss)
makedepends=(aria2)
install=${pkgname}.install
source=("${pkgname}.install")
sha256sums=('afba3c6712227a37c08783b3cc1a97ae71e90dc2f575409213d2773372220697')

prepare() {
    aria2c --max-concurrent-downloads=10 --max-connection-per-server=10 --split=10 https://lceda.cn/page/legal --out=LICENSE
    aria2c --max-concurrent-downloads=10 --max-connection-per-server=10 --split=10 https://image.lceda.cn/files/${pkgname}-linux-x64-${pkgver}.zip
    bsdtar --extract --file ${pkgname}-linux-x64-${pkgver}.zip --directory .
}

package() {
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
    if [ -f icon/icon_512x512@2x.png ]; then
        install -Dm644 icon/icon_512x512@2x.png \
                       ${pkgdir}/usr/share/icons/hicolor/1024x1024/apps/${pkgname}.png
    fi

    # desktop entry
    if [ -f lceda-pro.dkt ]; then
        install -Dm0644 lceda-pro.dkt \
                       ${pkgdir}/usr/share/applications/${pkgname}.desktop

        sed -i 's|/opt/lceda-pro/icon/icon_128x128.png|lceda-pro|g' \
            ${pkgdir}/usr/share/applications/${pkgname}.desktop
        sed -i 's|/opt/lceda-pro/||g' \
            ${pkgdir}/usr/share/applications/${pkgname}.desktop
    else
        install -Dm644 /dev/stdin $pkgdir/usr/share/applications/${pkgname}.desktop << "EOF"
[Desktop Entry]
Categories=Development;Electronics;
Comment=免费、强大、易用的在线电路设计软件
Exec=lceda-pro %f
Keywords=PCB;LCEDA;嘉立创EDA;LC;EDA
GenericName=嘉立创EDA(专业版)
Icon=lceda-pro
Name=嘉立创EDA(专业版)
Type=Application
Name[en_US]=LCEDA Pro
MimeType=application/eprj
EOF
    fi

    # lceda-pro file
    install -Dm0755 /dev/stdin ${pkgdir}/usr/bin/${pkgname} << EOF
#!/bin/sh

exec electron /usr/lib/lceda-pro/resources/app/ "\$@"
EOF
    # LICENSE
    install -Dm0644 ${srcdir}/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
