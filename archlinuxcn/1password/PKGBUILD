pkgname=1password
_tarver=8.0.32
_tar="${pkgname}-${_tarver}.tar.gz"
pkgver=${_tarver//-/_}
pkgrel=1
pkgdesc="Password manager and secure wallet"
arch=('x86_64')
url='https://1password.com'
license=('LicenseRef-1Password-Proprietary')
depends=('hicolor-icon-theme')
options=(!strip)
install="${pkgname}.install"
source=(https://downloads.1password.com/linux/tar/${_tar}{,.sig})
sha256sums=('78e207b4e70d4fff86e71eb3300c543427fc993263611bad20bd5e74a481cbe9'
            '78760f2c792c6a46af8139ac75ff3f2a9ab96c6f1dac6967c7ce9be61dd287d8'
)
validpgpkeys=('3FEF9748469ADBE15DA7CA80AC2D62742012EA22')

package() {
    # Go to source directory
    cd "${pkgname}-${_tarver}"

    # Install icons
    icons=(usr/share/icons/hicolor/*/${pkgname}.png)
    for icon in "${icons[@]}"
    do
        install -Dm0644 "${icon}" "${pkgdir}/${icon}"
    done
    # Install desktop file
    install -Dm0644 usr/share/applications/${pkgname}.desktop -t "${pkgdir}"/usr/share/applications/
    # Install system unlock PolKit policy file
    install -Dm0644 com.1password.1Password.policy -t "${pkgdir}"/usr/share/polkit-1/actions/

    # Move package contents to /opt/1Password
    cd "${srcdir}"
    install -dm0755 "${pkgdir}"/opt
    mv "${pkgname}-${_tarver}" "${pkgdir}/opt/1Password"

    # Symlink /usr/bin executable to opt
    install -dm0755 "${pkgdir}"/usr/bin
    ln -s /opt/1Password/${pkgname} "${pkgdir}"/usr/bin/${pkgname}
}
