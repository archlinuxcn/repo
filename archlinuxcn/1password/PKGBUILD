# Maintainer: Winston Astrachan <winston dot astrachan at gmail dot com>

pkgname=1password
pkgver=0.9.0.30138
pkgrel=1
_appimagver=0.9.0
_appimage="${pkgname}-${pkgver}-${pkgrel}.AppImage"
pkgdesc="The world's most-loved password manager - beta"
arch=('x86_64')
url='https://1password.com/'
license=('unknown')
depends=('fuse2' 'zlib' 'hicolor-icon-theme')
options=(!strip)
source=("${_appimage}::https://onepassword.s3.amazonaws.com/linux/appimage/1password-${_appimagver}.AppImage"
        "${_appimage}.sig::https://onepassword.s3.amazonaws.com/linux/appimage/1password-${_appimagver}.AppImage.sig"
)
noextract=("${_appimage}")
sha256sums=('97873170041b79d3795ae30213e1cf2582a1eba3b86b083f3abe844234d53281'
            'SKIP'
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
