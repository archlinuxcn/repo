pkgname=1password

_tarver=8.0.33-92.BETA
_tar="${pkgname}-${_tarver}.x64.tar.gz"
pkgver=${_tarver//-/_}
pkgrel=92
pkgdesc="Password manager and secure wallet"
arch=('x86_64')
url='https://1password.com'
license=('LicenseRef-1Password-Proprietary')
depends=('hicolor-icon-theme')
options=(!strip)
install="${pkgname}.install"
source=(https://downloads.1password.com/linux/tar/beta/x86_64/${_tar}{,.sig})
sha256sums=('f2f3223aea7c9470ed5f7def7519fab5e33d30b58c822596901434493c319026'
            '467a2120ae11b30040d20b2078071cc48ccfc35e0dbce66e112caf22bd415d96'
)
validpgpkeys=('3FEF9748469ADBE15DA7CA80AC2D62742012EA22')

package() {
    # Go to source directory
    cd "${pkgname}-${_tarver}.x64"

    # Install icons
    resolutions=(32x32 64x64 256x256 512x512)
    for resolution in "${resolutions[@]}"
    do
        install -Dm0644 "resources/icons/hicolor/${resolution}/apps/${pkgname}.png" \
            "${pkgdir}/usr/share/icons/hicolor/${resolution}/apps/${pkgname}.png"
    done
    # Install desktop file
    install -Dm0644 resources/${pkgname}.desktop -t "${pkgdir}"/usr/share/applications/
    # Install system unlock PolKit policy file
    install -Dm0644 com.1password.1Password.policy -t "${pkgdir}"/usr/share/polkit-1/actions/

    # Install examples
    install -Dm0644 resources/custom_allowed_browsers -t "${pkgdir}"/usr/share/doc/${pkgname}/examples/

    # Move package contents to /opt/1Password
    cd "${srcdir}"
    install -dm0755 "${pkgdir}"/opt
    mv "${pkgname}-${_tarver}.x64" "${pkgdir}/opt/1Password"

    # Symlink /usr/bin executable to opt
    install -dm0755 "${pkgdir}"/usr/bin
    ln -s /opt/1Password/${pkgname} "${pkgdir}"/usr/bin/${pkgname}
}
