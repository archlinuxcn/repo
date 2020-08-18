# Maintainer: Winston Astrachan <winston dot astrachan at gmail dot com>

pkgname=1password
pkgver=0.8.2.1.23842
pkgrel=1
pkgdesc="The world's most-loved password manager - read-only development preview"
arch=('x86_64')
url='https://1password.com/'
license=('unknown')
depends=('fuse3' 'zlib' 'hicolor-icon-theme')
makedepends=('sed')
options=(!strip)
_appimage="${pkgname}-${pkgver}.AppImage"
source=("${_appimage}::https://onepassword.s3.amazonaws.com/linux/appimage/1password-latest.AppImage")
noextract=("${_appimage}")
sha256sums=('4a131125385850f80397896d0fc0fa24fd3acc4caa600de6b94f02917347b83f')

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
