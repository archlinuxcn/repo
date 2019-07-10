# Maintainer: fthiery fthiery@gmail.com

pkgname=keeweb-desktop
pkgver=1.8.2
pkgrel=2
pkgdesc="This webapp is a desktop password manager compatible with KeePass databases."
arch=('x86_64')
depends=('gconf' 'libxss' 'gtk2')
optdepends=('xdotool: for Auto-type feature')
url="https://github.com/keeweb/keeweb"
license=('MIT')
source=(
    "${url}/releases/download/v${pkgver}/KeeWeb-${pkgver}.linux.x64.zip"
    "keeweb.desktop"
    "keeweb.xml"
)
sha256sums=('f6e6af159d302f83a9060597915cd64d315ad4a6b32b6d583d189e0bde88e82c'
            'd6a5d6402d4c1c211da5f077b77422fc7da4dd4c7208bc77e7e29cf2f5427ca3'
            '3d017c17a8788166c644e2460ba3596fd503f300342561921201fe5f69e5d194')

package(){
    mkdir -p "${pkgdir}"/opt/${pkgname}
    cp --preserve=mode -r * "${pkgdir}"/opt/${pkgname}
    rm ${pkgdir}/opt/${pkgname}/KeeWeb-${pkgver}.linux.x64.zip

    desktop-file-install -m 644 --dir "$pkgdir"/usr/share/applications/ keeweb.desktop

    for res in 128x128; do
        install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
        install -Dm755 ${pkgdir}/opt/${pkgname}/128x128.png ${pkgdir}/usr/share/icons/hicolor/${res}/apps/keeweb.png
    done


    mkdir -p "${pkgdir}"/usr/bin
    echo -e "#!/bin/sh\n/opt/${pkgname}/KeeWeb --disable-updater \$1" > ${pkgdir}/usr/bin/KeeWeb
    chmod 755 ${pkgdir}/usr/bin/KeeWeb

    install -Dm644 keeweb.xml "$pkgdir"/usr/share/mime/packages/keeweb.xml
}
