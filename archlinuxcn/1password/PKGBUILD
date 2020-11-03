pkgname=1password
pkgver=0.9.2_1
pkgrel=1
_appimagver=${pkgver//_/-}
_appimage="${pkgname}-${_appimagver}.AppImage"
pkgdesc="The world's most-loved password manager - beta"
arch=('x86_64')
url='https://1password.com/'
license=('unknown')
depends=('fuse2' 'zlib' 'hicolor-icon-theme')
options=(!strip)
source=("${_appimage}::https://downloads.1password.com/linux/appimage/${_appimage}"
        "${_appimage}.sig::https://downloads.1password.com/linux/appimage/${_appimage}.sig"
)
noextract=("${_appimage}")
sha256sums=('9902199d28312083df96ea63a74ec81c4b11162b9127b5ba39fffd56a1c3a8a6'
            'ded7f6d0296233b0b3932952386f4a5083ffe3ae9390981f68e701b2d934c935'
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
