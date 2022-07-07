pkgname=icalingua++
_pkgname=icalingua
pkgver=2.6.6
pkgrel=1
pkgdesc='A branch of deleted Icalingua,with limited support'
license=('AGPL3')
depends=('ffmpeg' 'electron' 'libappindicator-gtk3')
optdepends=('mongodb-bin: Provides storage'
            'redis: Provides storage')
arch=('aarch64' 'x86_64' 'i686')
url="https://github.com/Icalingua-plus-plus/Icalingua-plus-plus"
provides=('electron-qq' 'icalingua')
conflicts=('electron-qq')
replaces=('electron-qq' "icalingua-plus-plus")
source=(512x512.png
        ${_pkgname}.desktop
        ${_pkgname})
source_x86_64=("app-x86_64-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-x86_64.asar")
source_aarch64=("app-aarch64-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-arm64.asar")
source_i686=("app-i686-${pkgver}.asar::https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v${pkgver//_/-}/app-ia32.asar")

package() {
    install -Dm644 -t "${pkgdir}/usr/share/applications" "${_pkgname}.desktop"
    install -Dm644 "512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$_pkgname.png"
    install -Dm644 "app-${CARCH}-${pkgver}.asar" "${pkgdir}/usr/lib/${_pkgname}/${_pkgname}.asar"
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    ln -s "/usr/bin/${_pkgname}" "${pkgdir}/usr/bin/electron-qq"
}
sha256sums=('84c8585e8c18504ed83b0d199831b55b9f8f0eb0a5aa4cb9e3dc01b4a17d0e38'
            '43da1c99b7a6aee974c20da3bcf925b660dff4ba44a447c86066c84c8bc95fbd'
            '71a583dae6d4352481bed0062c82558c627be0dd4917f2179e7d41c46d51d5eb')
sha256sums_aarch64=('4354a0227c6fa306c8ec9c1a266742ff0120429f076cc9ab28722ff4b62a3d94')
sha256sums_x86_64=('dd24761e7730891ec055e1097cc0cab47515226be06a5f62abd696e1c09f19ee')
sha256sums_i686=('acd1ff5c7771f3f2648ce98ff7389f5ba260a33f486cda26f6c746bd799f508b')
