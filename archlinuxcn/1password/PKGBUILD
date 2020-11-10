pkgname=1password
_appimagver=0.9.3
_appimage="${pkgname}-${_appimagver}.AppImage"
pkgver=${_appimagver//-/_}
pkgrel=1
pkgdesc="Password manager and secure wallet"
arch=('x86_64')
url='https://1password.com/'
license=('LicenseRef-1Password-Proprietary')
depends=('fuse2' 'zlib' 'hicolor-icon-theme')
options=(!strip)
source=("${_appimage}::https://downloads.1password.com/linux/appimage/${_appimage}"
        "${_appimage}.sig::https://downloads.1password.com/linux/appimage/${_appimage}.sig"
)
noextract=("${_appimage}")
sha256sums=('c0ed47c1797a2dfefed9f5d7ee2f27ac3fe18bd7405a7e74264a33b71e9a4f44'
            '4c01893be04fc719b9174a7f283332610305f0a740c8279e8c57b07f6366fbb7'
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
