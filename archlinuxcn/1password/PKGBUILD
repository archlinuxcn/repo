# Maintainer: Winston Astrachan <winston dot astrachan at gmail dot com>

pkgname=1password
pkgver=0.8.10.29215
pkgrel=1
_appimagver=0.8.10
_appimage="${pkgname}-${pkgver}-${pkgrel}.AppImage"
pkgdesc="The world's most-loved password manager - development preview"
arch=('x86_64')
url='https://1password.com/'
license=('unknown')
depends=('fuse2' 'zlib' 'hicolor-icon-theme')
options=(!strip)
source=("${_appimage}::https://onepassword.s3.amazonaws.com/linux/appimage/1password-${_appimagver}.AppImage"
        "${_appimage}.sig::https://onepassword.s3.amazonaws.com/linux/appimage/1password-${_appimagver}.AppImage.sig"
)
noextract=("${_appimage}")
sha256sums=('b59ea9b1dc6e7bb2db19e45d7d1b136c1ce8209fab1490f9d8d4891ad83bb84b'
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
