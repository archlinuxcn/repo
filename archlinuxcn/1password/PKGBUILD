pkgname=1password

_tarver=8.0.33-26.BETA
_tar="${pkgname}-${_tarver}.tar.gz"
pkgver=${_tarver//-/_}
pkgrel=26
pkgdesc="Password manager and secure wallet"
arch=('x86_64')
url='https://1password.com'
license=('LicenseRef-1Password-Proprietary')
depends=('hicolor-icon-theme')
options=(!strip)
install="${pkgname}.install"
source=(https://downloads.1password.com/linux/tar/${_tar}{,.sig})
sha256sums=('2cbcdd3ab34aeea04fbdfcb286c3b425c7cd35d4726abd21ac1e1ca5ee142b6c'
            'f2d40812bb474adc915490e8232e61a321609188e26a918b0a49aed6f8f7ffb8'
)
validpgpkeys=('3FEF9748469ADBE15DA7CA80AC2D62742012EA22')

package() {
    # Go to source directory
    cd "${pkgname}-${_tarver}"

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
    mv "${pkgname}-${_tarver}" "${pkgdir}/opt/1Password"

    # Symlink /usr/bin executable to opt
    install -dm0755 "${pkgdir}"/usr/bin
    ln -s /opt/1Password/${pkgname} "${pkgdir}"/usr/bin/${pkgname}
}
