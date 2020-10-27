# Maintainer: Winston Astrachan <winston dot astrachan at gmail dot com>

pkgname=1password
pkgver=0.9.1
pkgrel=1
_appimagver=0.9.1
_appimage="${pkgname}-${pkgver}-${pkgrel}.AppImage"
pkgdesc="The world's most-loved password manager - beta"
arch=('x86_64')
url='https://1password.com/'
license=('unknown')
depends=('fuse2' 'zlib' 'hicolor-icon-theme')
options=(!strip)
source=("${_appimage}::https://downloads.1password.com/linux/appimage/1password-${_appimagver}.AppImage"
        "${_appimage}.sig::https://downloads.1password.com/linux/appimage/1password-${_appimagver}.AppImage.sig"
)
noextract=("${_appimage}")
sha256sums=('5fa36d372d55ed7ba81d68e329a42fb3889e2da009be37dc2cc60d4d383c1b12'
            '78ec2888c539194946cad4b220d0761da5d0333dd540d7ef491c20aa3d2f10d3'
)
validpgpkeys=('3FEF9748469ADBE15DA7CA80AC2D62742012EA22')

prepare() {
    chmod +x "${_appimage}"
    ./"${_appimage}" --appimage-extract
}

package() {
    cd "$srcdir"

    # Create Directories
    install -d "${pkgdir}/usr/bin"
    install -dm755 "${pkgdir}/usr/share/icons/hicolor"

    # Install AppImage
    install -Dm755 "${_appimage}" -t "${pkgdir}/opt/${pkgname}"

    # Install Icons, Desktop Shortcut
    find squashfs-root -type d -exec chmod 0755 {} \;
    cp -r squashfs-root/usr/share/icons/hicolor "${pkgdir}/usr/share/icons/"
    sed -i -E "s|Exec=AppRun|Exec=env DESKTOPINTEGRATION=false /usr/bin/${pkgname}|" "squashfs-root/${pkgname}.desktop"
    install -Dm644 "squashfs-root/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"

    # Symlink AppImage
    ln -s "/opt/${pkgname}/${_appimage}" "${pkgdir}/usr/bin/${pkgname}"
}
