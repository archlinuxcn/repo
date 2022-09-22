pkgname=icalingua++
_pkgname=icalingua
pkgver=2.7.3
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
sha256sums_aarch64=('c8e668ffc7dab9ed3d9827716ea30d9dbf03958ca0c84471087e569949509a23')
sha256sums_x86_64=('05bbd31ad23aefa172d4027ad6b4d1591895ca0e4c203153bdddff81f1f68fc5')
sha256sums_i686=('a385f7d8d593685c294d9fadcb57cd33546861087716627d9f591f0330d642ac')
